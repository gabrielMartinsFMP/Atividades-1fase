import os
import html
import sys


def is_text_file(path):
    # simple filter by extension
    text_exts = {'.py', '.java', '.c', '.cpp', '.h', '.txt', '.md', '.alg', '.js', '.html', '.css'}
    _, ext = os.path.splitext(path)
    return ext.lower() in text_exts


def collect_files(root):
    tree = {}
    for dirpath, dirnames, filenames in os.walk(root):
        rel = os.path.relpath(dirpath, root)
        parts = [] if rel == '.' else rel.split(os.sep)
        node = tree
        for p in parts:
            node = node.setdefault(p, {})
        files = []
        for f in sorted(filenames):
            full = os.path.join(dirpath, f)
            if is_text_file(full):
                files.append((f, full))
        if files:
            node['_files'] = files
    return tree


def render_tree(node, id_prefix=''):
    html_parts = ['<ul class="tree">']
    idx = 0
    for name, child in sorted(node.items()):
        if name == '_files':
            for fname, fpath in child:
                fid = ffile_id(fpath)
                html_parts.append(f'<li class="file" data-path="{html.escape(fpath)}">'
                                  f'📄 <a href="#" data-fileid="{fid}">{html.escape(fname)}</a></li>')
            continue
        fid_prefix = f"{id_prefix}{idx}_"
        html_parts.append(f'<li class="folder">📁 <span class="folder-name">{html.escape(name)}</span>')
        html_parts.append(render_tree(child, fid_prefix))
        html_parts.append('</li>')
        idx += 1
    html_parts.append('</ul>')
    return '\n'.join(html_parts)


def ffile_id(path):
    return 'f' + str(abs(hash(path)))


def embed_files(node, out):
    # recursively embed files as <pre><code id="{id}">...
    for k, v in node.items():
        if k == '_files':
            for fname, fpath in v:
                fid = ffile_id(fpath)
                try:
                    with open(fpath, 'r', encoding='utf-8', errors='replace') as fh:
                        content = fh.read()
                except Exception:
                    content = ''
                out.append(f'<div class="code-block" id="{fid}" data-path="{html.escape(fpath)}">')
                out.append(f'<h3>{html.escape(fname)}</h3>')
                out.append('<pre><code>')
                out.append(html.escape(content))
                out.append('</code></pre>')
                out.append('</div>')
        else:
            embed_files(v, out)


HTML_TMPL = '''<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Programação Estruturada I - Viewer</title>
  <style>
    body{font-family: Arial, Helvetica, sans-serif; display:flex; gap:20px; padding:20px}
    .sidebar{width:320px; max-height:90vh; overflow:auto; border-right:1px solid #ddd; padding-right:12px}
    .content{flex:1; max-height:90vh; overflow:auto}
    ul.tree{list-style:none; padding-left:18px}
    li.folder > .folder-name{cursor:pointer; font-weight:600}
    li.folder ul{display:none}
    li.folder.open > ul{display:block}
    li.file{margin:4px 0}
    .code-block{display:none}
    .code-block.active{display:block}
    pre{background:#f6f8fa;padding:12px;border-radius:6px;overflow:auto}
  </style>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/styles/default.min.css">
</head>
<body>
  <div class="sidebar">
    <h2>Programação Estruturada I</h2>
    {tree_html}
  </div>
  <div class="content">
    <div id="viewer">Escolha um arquivo na árvore à esquerda.</div>
    {embedded}
  </div>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/highlight.min.js"></script>
  <script>hljs.highlightAll();</script>
  <script>
    document.querySelectorAll('li.folder .folder-name').forEach(el=>{
      el.addEventListener('click', ()=> el.parentElement.classList.toggle('open'))
    })
    document.querySelectorAll('li.file a').forEach(a=>{
      a.addEventListener('click', e=>{
        e.preventDefault();
        const id = a.dataset.fileid;
        document.querySelectorAll('.code-block').forEach(b=>b.classList.remove('active'));
        const block = document.getElementById(id);
        if(block){ block.classList.add('active'); block.scrollIntoView({behavior:'smooth'}); }
      })
    })
  </script>
</body>
</html>
'''


def main(target_dir=None, out_file=None):
    base = os.path.dirname(__file__)
    if target_dir is None:
        target_dir = os.path.join(base, '2FASE', 'Programação Estruturada I')
    if out_file is None:
        out_file = os.path.join(base, 'Programacao_Estruturada_I_viewer.html')
    if not os.path.isdir(target_dir):
        print('Pasta alvo não encontrada:', target_dir)
        return
    tree = collect_files(target_dir)
    tree_html = render_tree(tree)
    embedded = []
    embed_files(tree, embedded)
    full = HTML_TMPL.format(tree_html=tree_html, embedded='\n'.join(embedded))
    with open(out_file, 'w', encoding='utf-8') as fh:
        fh.write(full)
    print('Gerado:', out_file)


if __name__ == '__main__':
    arg_dir = sys.argv[1] if len(sys.argv) > 1 else None
    arg_out = sys.argv[2] if len(sys.argv) > 2 else None
    main(arg_dir, arg_out)
