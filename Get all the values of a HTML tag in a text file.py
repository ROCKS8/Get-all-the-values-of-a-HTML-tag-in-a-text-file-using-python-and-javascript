# Importing necessary modules

try:

    import webbrowser
    import sys
    import os
except:
    print("Could not import modules!!!")
else:
    pass

#Start

try:
    print("Get all the values of a HTML tag in a text file!!!!\n")

    command = "curl --output Src_code.html " + input("Enter URL: ")
    os.system("start /wait cmd /c {c}".format(c=command))

    # All valid html tags
    validTags = ["a", "abbr", "address", "area", "article", "audio", "aside", "b", "base", "bdi", "bdo", "blockquote", "body", "br", "button", "canvas", "caption", "cite", "code", "col", "colgroup", "data", "datalist", "dd", "del", "details", "dfn", "dialog", "div", "dl", "em", "embed", "fieldset", "figcaption", "figure", "footer", "form", "head", "header", "hgroup", "h1", "h2", "h3", "h4", "h5", "h6", "hr", "html", "i", "iframe", "img", "input", "ins", "kbd", "label", "legend", "li", "link", "main", "map", "mark", "meta", "meter", "nav", "noscript", "object", "p", "param", "picture", "pre", "progress", "q", "rp", "rt", "ruby", "s", "samp", "script", "section", "select", "small", "source", "strong", "span", "style", "sub", "svg", "table", "tbody", "td", "template", "textarea", "th", "thead", "time", "tr", "track", "u", "ul", "var", "video", "wbr"]

    # Taking Input of tag name, give input without angular brackets

    while(True):
        temp = False
        try:
            tagInput = input("Please enter the HTML Tag: ")
            for i in validTags:
                if ( i == tagInput):
                    temp = True
                    break
            if (temp == True):
                break
            else:
                print("Please enter a valid tag!!!")
                continue
        except:
            print("Something went wrong!!!")
        else:
            pass

    # Creating file Src_code.html

    file = open("Src_code.html", "a", encoding="utf-8")

    # Input string for javascript which contains download function and logic for getting all the values of a tag.

    inp_str = """\n <script>

function download(strData, strFileName, strMimeType) {
    var D = document,
        A = arguments,
        a = D.createElement("a"),
        d = A[0],
        n = A[1],
        t = A[2] || "text/plain";

    a.href = "data:" + strMimeType + "charset=utf-8," + escape(strData);

    if (window.MSBlobBuilder) { 
        var bb = new MSBlobBuilder();
        bb.append(strData);
        return navigator.msSaveBlob(bb, strFileName);
    }


    if ('download' in a) {
        a.setAttribute("download", n);
        a.innerHTML = "downloading...";
        D.body.appendChild(a);
        setTimeout(function () {
            var e = D.createEvent("MouseEvents");
            e.initMouseEvent("click", true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            a.dispatchEvent(e);
            D.body.removeChild(a);
        }, 66);
        return true;
    }
}
    var alerrt = document.getElementsByTagName('"""

    inp_str += tagInput + """');
    var len = alerrt.length;
    var string = '';
    for (i = 0; i < len; i++){
        string += document.getElementsByTagName('"""


    inp_str += tagInput + """')[i].textContent + """

    inp_str += '"'+str(chr(92) + chr(110))+'"'

    inp_str += """;
    }
    download(string, 'download.txt', 'text/plain');


</script>"""

    # writing input string to the file and closing the file
    text = file.write(inp_str)
    file.close()
    
    # Opening the file in browser
    webbrowser.open('Src_code.html')

except:
    print("Something went wrong, could not execute program!!!")
    sys.exit()
