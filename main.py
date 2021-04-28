import envControl.control as control
import envControl.tests as tests
import grow_flask.app as grow_flask




app = grow_flask.createApp()
#app.run()
app.run(host='0.0.0.0', port=80, debug=True)
