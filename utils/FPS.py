import datetime
import cv2

class FPS:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.frames_elapsed = 0
        self._fps = 0
        
    def start(self):
        self.start_time = datetime.datetime.now()
        return self

    def stop(self):
        self.end_time = datetime.datetime.now()

    def update(self):
        self.frames_elapsed += 1

    def fps_print(self, frame):
        diff = (self.end_time - self.start_time).total_seconds()
        fps = self.frames_elapsed / diff
        
        text = "FPS: {}".format(int(fps))
        cv2.putText(frame, text, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,0), 2)
        return frame
