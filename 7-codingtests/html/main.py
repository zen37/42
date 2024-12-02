def HTMLElements(strParam):
    stack = []  #track opening tags
    
    i = 0
    while i < len(strParam):
        if strParam[i] == "<":  # we detect the start of a tag
            j = i + 1
            while j < len(strParam) and strParam[j] != ">":  # find end of the tag
                j += 1
            
            if j == len(strParam):
                break  # n closing '>', exit loop (should not happen though, but better safe than sorry)
            
            tag = strParam[i + 1:j]
            
            if not tag.startswith("/"):  #opening tag
                stack.append(tag)
            else:  #closing tag
                if not stack:
                    return tag[1:]  #mismatched closing tag
                last_open_tag = stack.pop()
                if last_open_tag != tag[1:]:
                    return last_open_tag  #mismatched tags
            
            i = j
        i += 1
    
    if stack:
        return stack[-1]
    return "true"

  
if __name__ == "__main__":
    #input = "<div>hello world</div>"
    input = "<div><div>hello world</b></div>"
    print(HTMLElements(input))
