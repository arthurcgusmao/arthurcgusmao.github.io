import os, sys, subprocess
import frontmatter

def get_html_version(f):
    bashCommand = "pandoc --filter=/home/arthurcgusmao/.miniconda3/bin/pandoc-fignos --filter=/home/arthurcgusmao/.miniconda3/bin/pandoc-eqnos --filter=pandoc-citeproc {} -t html ".format(f)
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE, universal_newlines=True)
    output, error = process.communicate()
    return output

def get_final_post_front_matter(f):
    fm = frontmatter.load(f)
    d = fm.get('final_post_front_matter')
    s = "---\n"
    for key, value in d.items():
        s += "{}: {}\n".format(key, value)
    s += "---\n\n"
    return s

def write_final_post(fpath):
    name, ext = fpath.split('.')

    if ext != 'md':
        raise ValueError('It should be a markdown file, bro.')

    output = ""
    output += get_final_post_front_matter(fpath)
    output += get_html_version(fpath)

    with open('../_posts/{}.html'.format(name), 'w') as f:
        f.write(output)


_, file = sys.argv
write_final_post(file)
