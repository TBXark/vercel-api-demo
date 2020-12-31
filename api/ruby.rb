Handler = Proc.new do |req, res|
  name = req.query['name'] || 'NULL'
  res.status = 200
  res['Content-Type'] = 'text/text; charset=utf-8'
  res.body = "Ruby: Hello #{name}!"
end