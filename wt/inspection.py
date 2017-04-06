import json
from os.path import dirname, join, normpath
from watson_developer_cloud import VisualRecognitionV3


def main():
    visual_recognition = VisualRecognitionV3('2016-05-20', api_key='')
    target = normpath(join(dirname(__file__), '../img/ako.png'))
    with open(target, 'rb') as image_file:
        write('classify_result.json', json.dumps(visual_recognition.classify(images_file=image_file), indent=2))

    with open(target, 'rb') as image_file:
        write('detect_faces.json', json.dumps(visual_recognition.detect_faces(images_file=image_file), indent=2))

    with open(target, 'rb') as image_file:
        write('recognize_text.json', json.dumps(visual_recognition.recognize_text(images_file=image_file), indent=2))


def write(file_name, data):
    with open(file_name, 'wt') as file:
        file.write(data)


if __name__ == '__main__':
    main()
