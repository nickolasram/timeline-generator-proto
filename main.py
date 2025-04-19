from timeline import Timeline
from testing_data import landmarks
import random


def generate_relationships():
    max = len(landmarks) - 1
    for i in range(max + 1):
        relationships = set()
        if not landmarks[i].era:
            for j in range(random.randint(0, max-5)):
                index = random.randint(0, max)
                if index != i:
                    relationships.add(landmarks[index])
        landmarks[i].set_relationships(relationships)


if __name__ == "__main__":
    generate_relationships()
    x = Timeline()
    x.set_landmarks(landmarks)
    x.dump_data()
