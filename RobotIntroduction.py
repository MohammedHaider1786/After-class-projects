class Robot:
    def __init__(self, name, model, purpose):
        self.name = name
        self.model = model
        self.purpose = purpose

    def introduce(self):
        print("Hello! I am a robot.")
        print("My name is:", self.name)
        print("My model is:", self.model)
        print("My purpose is:", self.purpose)


def main():
    robot_name = input("Enter robot name: ")
    robot_model = input("Enter robot model: ")
    robot_purpose = input("Enter robot purpose: ")

    my_robot = Robot(robot_name, robot_model, robot_purpose)
    my_robot.introduce()


main()
