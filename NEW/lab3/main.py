from controller import Controller
from model import Model

if __name__ == "__main__":
    ''' Model creation. '''
    model = Model("source")

    ''' Controller creation. Use model as agruement. '''
    controller = Controller(model)

    ''' The start of console application. '''
    controller.start()
	
    ''' The save of the model. '''
    model.save()


