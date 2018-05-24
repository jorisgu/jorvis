import time
import numpy as np
from tqdm import tqdm

class jSource:
    """ class to deliver common formalism from source folder, camera, ROS node, webcam, video.... """
    def __init__(self):
        pass

    def get_data(self,t=None):
        return np.ones((200,400))


class jTracker:
    """ class of tracker """
    def __init__(self):
        self.objects = []

    def add_object(t, input_id, input_data, crop, mask=None):
        """ Allows to track a new object """
        pass

    def update(self,t,input_id, input_data):
        """ Allows to update position of tracked objects """
        pass



#Jorvis starts
if __name__=="__main__":
    sources=[jSource()]
    trackers =[jTracker()]
    for _ in tqdm(range(1000)):
        t = time.time()
        inputs = [source.get_data(t) for source in sources]
        for input_id,input_data in enumerate(inputs):
            for tracker in trackers:
                # print('c')
                tracker.update(t, input_id, input_data)

        time.sleep(0.01)

else:
    print("Not main")
