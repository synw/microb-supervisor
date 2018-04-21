var cmd = app.cmds[uid];
if (cmd !== undefined) {
	console.log("CMD", cmd.domain, message);
  	if (message === "The http server is running") {
	  	console.log("**********************SITE", data, "INST", app.instances);
  		app.instances[cmd.domain].status = "up"
	} else if (message === "The http server is not running") {
		app.instances[cmd.domain].status = "down"
	}
  	cmd.status = "success";
}