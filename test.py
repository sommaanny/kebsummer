import json
import os

# JSON 파일들이 있는 폴더 경로
json_folder_path = '/Users/osuman/Downloads/144.지자체_도로_정비_AI_데이터 2/01.데이터/2.Validation/라벨링데이터/VL01_지자체도로정비AI데이터_CASE1(도로)_WET_RAIN/지자체도로정비AI데이터_CASE1(도로)_WET_RAIN_03'
# 라벨 저장 폴더 경로
label_folder = '/Users/osuman/Downloads/new_data/export/labels'

# 클래스 ID 설정
class_labels = {
    1: 0,  # "도로균열"
    2: 1   # "도로(홀)"
}

# 폴더 생성
os.makedirs(label_folder, exist_ok=True)

# 모든 JSON 파일 처리
for json_file in os.listdir(json_folder_path):
    if json_file.endswith('.json'):
        json_file_path = os.path.join(json_folder_path, json_file)
        with open(json_file_path, 'r') as f:
            data = json.load(f)
        
        # 이미지 정보 처리
        images = {image['id']: image for image in data['images']}
        
        # 주석 정보 처리
        for annotation in data['annotations']:
            image_id = annotation['image_id']
            category_id = annotation['category_id']
            segmentation = annotation['segmentation'][0]
            
            # 바운딩 박스 계산
            x_coords = segmentation[0::2]
            y_coords = segmentation[1::2]
            x_min, x_max = min(x_coords), max(x_coords)
            y_min, y_max = min(y_coords), max(y_coords)
            bbox_width = x_max - x_min
            bbox_height = y_max - y_min
            x_center = (x_min + x_max) / 2
            y_center = (y_min + y_max) / 2

            # 이미지 정보
            image_info = images[image_id]
            image_filename = image_info['file_name']
            image_width = image_info['width']
            image_height = image_info['height']

            # 정규화
            x_center /= image_width
            y_center /= image_height
            bbox_width /= image_width
            bbox_height /= image_height

            # 라벨 파일 작성
            label_file_path = os.path.join(label_folder, os.path.splitext(image_filename)[0] + '.txt')
            with open(label_file_path, 'a') as lf:
                lf.write(f'{class_labels[category_id]} {x_center} {y_center} {bbox_width} {bbox_height}\n')

print("모든 라벨 파일이 생성되었습니다.")
