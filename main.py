import time
import numpy as np
from tqdm import tqdm
import cv2
import sys

class jSource:
    """ class to deliver common formalism from source folder, camera, ROS node, webcam, video, google research, wikipedia.... """
    def __init__(self,name):
        self.name = name
        self.last_update_time = -1
    def get_data(self, t=None):
        if t is None:
            t = time.time()
        try:
            data = self._get_data(t)
            if data is not None:
                self.last_update_time = t
            return data
        except:
            return None

    # def _get_data(self,t=None):
    #     print("Not implemented")
    #     return None
        # return np.ones((200,400))

class jSourceImage(jSource):
    def __init__(self, name, img_path):
        super().__init__(name)
        self.img_path = img_path
        self.img = cv2.imread(self.img_path)
    def _get_data(self,t=None):
        return self.img

class jSourceVideo(jSource):
    def __init__(self, name, video_path):
        super().__init__(name)
        self.video_path = video_path
        self.video = cv2.VideoCapture(video_path)
        # print(name, video_path, "Is opened ?",self.video.isOpened())
    def _get_data(self,t=None):
        if not self.video.isOpened():
            # print ("Could not open video")
            return None
            # sys.exit()

        # Read first frame.
        ok, frame = self.video.read()
        if not ok:
            # print ('Cannot read video file')
            return None
            # sys.exit()
        return frame



class jTracker:
    """ class of tracker """
    def __init__(self):
        self.objects = []

    def add_object(t, source_id, input_data, crop, mask=None):
        """ Allows to track a new object """
        pass

    def update(self,t,source_id, input_data):
        """ Allows to update position of tracked objects """
        pass



#Jorvis starts
if __name__=="__main__":
    sources=[]
    # sources.append(jSourceImage("image_test","/app/images/image1.jpg"))
    sources.append(jSourceVideo("video_test",'/app/videos/car_racing.mp4'))
    trackers =[jTracker()]



    pbar = tqdm(range(100000))
    last_var = None
    for _ in pbar:
        time.sleep(0.01)

        t = time.time()
        for source_id,source in enumerate(sources):
            input_data = source.get_data(t)
            if input_data is None:
                #
                continue

            last_var=np.var(input_data)
            # add object to trackers


            # track objects

            for tracker_id,tracker in enumerate(trackers):
                # print('c')
                tracker.update(t, source_id, input_data)


            # try:
        pbar.set_postfix(var=last_var ,t=str(t), last_up_t=str(source.last_update_time))
            # except:
            #     pass



else:
    print("Not main")
