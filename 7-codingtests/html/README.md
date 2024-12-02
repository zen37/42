find malformed html:
1. <div>hello world</div> => return "true"
2. <div><div>hello world</b></div> => return "div" (first tag that should be changed so that html is well formed)