# vercel-api-demo


### Golang
[https://vercel-api-demo.tbxark.vercel.app/api/go?name=World](https://vercel-api-demo.tbxark.vercel.app/api/go?name=World)
```go
package handler

import (
	"fmt"
	"net/http"
)

func Handler(w http.ResponseWriter, r *http.Request) {
	name := r.URL.Query().Get("name")
	if name == "" {
		name = "NULL"
	}
	fmt.Fprintf(w, "Golang: Hello %s!", name)
}
```
---



### Ruby
[https://vercel-api-demo.tbxark.vercel.app/api/ruby?name=World](https://vercel-api-demo.tbxark.vercel.app/api/ruby?name=World)
```ruby
Handler = Proc.new do |req, res|
  name = req.query['name'] || 'NULL'
  res.status = 200
  res['Content-Type'] = 'text/text; charset=utf-8'
  res.body = "Ruby: Hello #{name}!"
end
```
---



### Python
[https://vercel-api-demo.tbxark.vercel.app/api/python?name=World](https://vercel-api-demo.tbxark.vercel.app/api/python?name=World)
```python
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        data = [x for i,x in enumerate(self.path.split("?")[1].split("&")) if x.split("=")[0] == "name"]
        name = "NULL"
        if len(data) > 0:
            name = data[0].split("=")[1]
        self.wfile.write(("Python: Hello %s!" % name).encode())
        return
```
---



### TypeScript
[https://vercel-api-demo.tbxark.vercel.app/api/typescript?name=World](https://vercel-api-demo.tbxark.vercel.app/api/typescript?name=World)
```typescript
import { NowRequest, NowResponse } from '@vercel/node'

export default function (req: NowRequest, res: NowResponse) {
    const { name = 'NULL' } = req.query
    res.send(`Typescript: Hello ${name}!`)
}
```
---



### JavaScript
[https://vercel-api-demo.tbxark.vercel.app/api/javascript?name=World](https://vercel-api-demo.tbxark.vercel.app/api/javascript?name=World)
```javascript
module.exports = (req, res) => {
    const { name = 'World' } = req.query
    res.send(`JavaScript: Hello ${name}!`)
}
```
