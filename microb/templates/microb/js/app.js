{% load microb_tags %}
const app = new Vue({
	el: '#app',
	delimiters : ['{!', '!}'],
	mixins: [vvMixin],
    data () {
        return {
        	instances: {{% for instance in instances %}
        		"{{ instance.domain}}": {
        			"domain": "{{ instance.domain }}",
        			"url": "{{ instance.url }}",
        			"status": "Unknown"
        		}{% if not forloop.last %},{% endif %}
        	{% endfor %}
        	},
        	cmds: {},
        }
	},
	methods: {
		cmd: function(name, service, args) {
			var id = Math.random().toString(36).substr(2, 12);
			var payload = {
				"Id": id,
				"Name": name,
				"Service": service,
				"Args": args,
				"From": "browser",
				"Domain": "{{ instance.domain }}",
				"Status": "pending",
				"ErrMsg": "",
				"Date": new Date(Date.now()).toISOString()
			}
			return payload
		},
		runCmd: function(cmd, instance) {
			setTimeout(function(){
				if (cmd !== undefined) {
					instance.status = "down";
					delete cmd
				}
			}, 10000);
		},
		ping: function(sub, instance) {
			var payload = this.cmd("ping", "infos", []);
			this.cmds[payload.Id] = "pending";
			//if (instance.status !== "up") {
				instance.status = "Pinging..."
			//}
			this.cmds[payload.Id] = {"domain": instance.domain, "status": "published"};
			this.runCmd(this.cmds[payload.Id], instance);
			sub.publish(payload).then(function() {
		        //console.log("ID", this.cmds[payload.Id], sub.channel);
		        //instance.status = "up"
		    }, function(err) {
		    	delete this.cmds[payload.Id]
		    	instance.status = "error"
		    });
		},
	},
});

{% for instance in instances %}
	var sub_{{forloop.counter}} = cmd_{{instance.domain}}_in_subscription;
	app.ping(sub_{{forloop.counter}}, app.instances.{{instance.domain}});
	setInterval(function(){
		//console.log("PING", "{{instance.domain}}", sub)
		app.ping(sub_{{forloop.counter}}, app.instances.{{instance.domain}});
	}, 10000);
{% endfor %}

