{% load microb_tags %}
const app = new Vue({
	el: '#app',
	delimiters : ['{!', '!}'],
	mixins: [vvMixin],
    data () {
        return {
        	instances: {{% for instance in instances %}
        		"{{ instance.slug}}": {
        			"domain": "{{ instance.domain }}",
        			"url": "{{ instance.url }}",
        			"status": "Unknown"
        		}{% if not forloop.last %},{% endif %}
        	{% endfor %}
        	},
        }
	},
	methods: {
		cmd: function(name, service, args) {
			var payload = {
				"Name": name,
				"Service": service,
				"Args": args,
				"From": "browser",
				"Status": "pending",
				"ErrMsg": "",
				"Date": new Date(Date.now()).toISOString()
			}
			return payload
		},
		ping: function(sub, instance) {
			var payload = this.cmd("ping", "infos", []);
			instance.status = "Pinging..."
			sub.publish(payload).then(function() {
		        console.log("SUCCESS");
		        console.log("INSTANCE", instance);
		        instance.status = "up"
		    }, function(err) {
		    	console.log("ERR");
		    	instance.status = "down"
		    });
		},
	},
});

{% for instance in instances %}
	var sub = cmd_{{instance.domain}}_in_subscription;
	app.ping(sub, app.instances.{{instance.domain}});
	setInterval(function(){
		console.log("PING", sub)
		app.ping(sub, app.instances.{{instance.domain}});
	}, 10000);
{% endfor %}

