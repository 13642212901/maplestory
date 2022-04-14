import thread
import units
import units as u
import cv2

DANGER_TPL = "danger.jpg"

class Danger(thread.ThreadController):
    def handle(self):
        img = self.getScreen().get()
        ret1, thresh = cv2.threshold(img, 185, 255, cv2.THRESH_BINARY)
        tpl = cv2.imread(DANGER_TPL)
        res = u.match(tpl, thresh, 0.001)
        if (units.debug):
            print("danger:", res)
        if (res[0]):
            self.getAction().sendArray(["left", "right", "left", "right", "left", "right", "left", "right", "left", "right", "left", "right", "left", "right", "left", "right", "left", "right"])
