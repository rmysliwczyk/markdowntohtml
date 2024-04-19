import re

def convert(markdown_content : str):
    """
    Converts a string containing markdown into a string containing html
    """

    html_content = markdown_content

    #Headings
    for heading_level in range(3,0,-1):
        html_content = re.sub(
                r"^#{" + str(heading_level) + "}\s*(.*)",
                f"<h{heading_level}>\g<1></h{heading_level}>",
                html_content, flags=re.MULTILINE
            )

    #Bold text
    html_content = re.sub(r"\*{2}([^\*]*)\*{2}", f"<strong>\g<1></strong>", html_content)

    #Links
    html_content = re.sub(r"\[([^[\]]+)\]\(([^()]+)\)", f'<a href="\g<2>">\g<1></a>', html_content)

    #Unordered lists
    html_content = re.sub(r"^(?:\*|\+|-)+\s(.*)", f"<li>\g<1></li>", html_content, flags=re.MULTILINE)
    html_content = re.sub(r"(?<=\s\n)(<li>.*)", f"<ul>\n\g<1>", html_content)
    html_content = re.sub(r"(.*</li>)\n(?=\s)", f"\g<1>\n</ul>\n", html_content)

    #<p> tags
    html_content = re.sub(r"^[ ]*^((?!<h|<li|<ul|</ul).+)", f"<p>\g<1></p>", html_content, flags=re.MULTILINE)
    
    #Add empty line at end if none exist 
    html_content = re.sub(r"(\S){1}$", f"\g<1>\n", html_content)

    #Remove duplicated new lines
    html_content = re.sub(r"(.*)\n{2,}", f"\g<1>\n\n", html_content)

    #Remove extra empty lines at the end if needed
    html_content = re.sub(r"\s+$", f"\n", html_content)

    return html_content