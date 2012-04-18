class AnimationFrames(object):
    def __init__(self, frames, loops=-1):
        self._times = []
        self._data = []
        total = 0
        for t, data in frames:
            total += t
            self._times.append(total)
            self._data.append(data)

        self.end = total
        self.loops = loops
            

    def get(self, time):
        # if looping forever or within the number of loops, wrap time
        if self.loops == -1 or time < self.loops * self.end:
            time %= self.end
       
        # return last frame if we've gone too far
        if time > self.end:
            return self._data[-1]
        
        # otherwise loop until we get the right frame
        idx = 0
        while self._times[idx] < time:
            idx += 1

        return self._data[idx]




class Animation(object):
    def __init__(self, spritesheet, frames):
        if not isinstance(frames, AnimationFrames):
            frames = AnimationFrames(frames)

        self.spritesheet = spritesheet
        self.frames = frames
        self.time = 0
        self.update(0)

    def get_frame_data(self, time):
        return self.frames.get(time)

    def get_current_frame(self):
        return self.spritesheet.get(self.x, self.y)

    def update(self, dt):
        self.time += dt
        self.x, self.y = self.get_frame_data(self.time)

