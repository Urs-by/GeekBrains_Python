import controller

controller.callMainMenu()
value = controller.initValue()
while value != 0:
    controller.callButton()
    value = controller.initValue()
