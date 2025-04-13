from timeline import Timeline
from testing_data import landmarks


if __name__ == "__main__":
    x = Timeline()
    x.set_landmarks(landmarks)
    x.dump_data()