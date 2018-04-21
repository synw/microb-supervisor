String.prototype.trim = function(charlist) {
  return this.trimLeft(charlist).trimRight(charlist);
};
data = {
	"UID": payload.data.Id,
	"message": payload.data.ReturnValues.join(" ").trim(),
	"timestamp": payload.data.Date,
	"channel": payload.channel,
	"event_class": "Command",
	"site": payload.Domain,
	"data": {}
}
return data
