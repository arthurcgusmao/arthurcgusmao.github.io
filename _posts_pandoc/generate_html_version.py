import os
import sys
import subprocess

import frontmatter


def get_html_version(filename):
    bash_command = "pandoc"
    bash_command += f" --filter=pandoc-fignos"
    bash_command += f" --filter=pandoc-eqnos"
    bash_command += f" --filter=pandoc-citeproc {filename} -t html"
    process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE,
                               universal_newlines=True)
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


if ___name___ == "___main___":
    _, filename = sys.argv
    write_final_post(filename)
