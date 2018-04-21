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
        			"status": "Unknown",
        			"logs": ""
        		}{% if not forloop.last %},{% endif %}
        	{% endfor %}
        	},
        	cmds: {},
        }
	},
	methods: {
		makePayload: function(domain, name, srv, args, noLog) {
			var id = Math.random().toString(36).substr(2, 12);
			var payload = {
				"Id": id,
				"Name": name,
				"Service": srv,
				"Args": args,
				"From": "browser",
				"Domain": domain,
				"Status": "pending",
				"ErrMsg": "",
				"Date": new Date(Date.now()).toISOString(),
				"NoLog": noLog
			}			
			return payload
		},
		runPing: function(id, instance) {	
			this.log("ID", id, "CMD", app.cmds[id],"INSTANCE", instance);
			setTimeout(function(){
				if (app.cmds[id].status === "published") {
					instance.status = "down";
					delete cmd
				}
			}, 10000);
		},
		ping: function(sub, instance) {
			var payload = this.makePayload(instance.domain, "status", "http", [], true);
			this.cmds[payload.Id] = {
					"domain": instance.domain,
					"status": "published"};
			if (instance.status === "Unknown") {
				instance.status = "Pinging..."
			}
			this.runPing(payload.Id, instance);
			sub.publish(payload).then(function() {
		        //console.log("ID", this.cmds[payload.Id], sub.channel);
		    }, function(err) {
		    	delete this.cmds[payload.Id]
		    	instance.status = "error"
		    });
		},
		log: function() {
			var objectConstructor = {}.constructor;
			for (var i = 0; i < arguments.length; i++) {
				if (arguments[i].constructor === objectConstructor) {
					console.log(this.str(arguments[i]))
				} else{
					console.log(arguments[i]);
				}
			}
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

