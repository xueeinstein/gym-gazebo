import gym
import rospy
import roslaunch


class GazeboEnv(gym.Env):

	def __init__(self, launchfile_path):

		# Launch the simulation with the given launchfile name
		this.node = rospy.init_node('gym', anonymous=True)

		if model_path.startswith("/"):
            fullpath = launchfile_path
        else:
            fullpath = os.path.join(os.path.dirname(__file__), "assets/launch", launchfile_path)
        if not path.exists(fullpath):
            raise IOError("File %s does not exist"%fullpath)

		this.uuid = roslaunch.rlutitl.get_or_generate_uuid(None, False)
		this.launch = roslaunch.parent.ROSLaunchParent(uuid, fullpath)
		launch.start()


	def _spawn_robot(self):

		# TODO
		# Spawn robot
		# Optional
		# Another option is to spawn the robot in the __init__ method

	def _step(self, action):

		# TODO
		# Perform a step in gazebo. E.g. move the robot

	def _reset(self):

		# TODO
		# Reset world/simulation

	def _render(self, episodes):

		# Open GUI (if it's not allready opened?)
		# episodes = number of episodes that GUI is going to be opened. Another option is to use _close to close the gui

	def _close(self):

		# TODO
		# From OpenAI API: Perform any necessary cleanup

	def _configure(self):

		# TODO
		# From OpenAI API: Provides runtime configuration to the enviroment
		# Maybe set the Real Time Factor?

	def _seed(self):
		
		# TODO
		# From OpenAI API: Sets the seed for this env's random number generator(s)	