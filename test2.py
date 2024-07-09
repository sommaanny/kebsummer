import os

# 이미지 파일들이 있는 폴더 경로
image_folder = '/Users/osuman/Downloads/new_data/export/images'
# 텍스트 파일들이 있는 폴더 경로
text_folder = '/Users/osuman/Downloads/new_data/export/labels'

# 이미지 파일 이름 목록 생성 (확장자 제거)
image_files = {os.path.splitext(f)[0] for f in os.listdir(image_folder) if f.endswith(('.jpg', '.jpeg', '.png'))}

# 텍스트 파일 이름 목록 생성 (확장자 제거)
text_files = {os.path.splitext(f)[0] for f in os.listdir(text_folder) if f.endswith('.txt')}

# 이미지 파일 이름에 해당하지 않는 텍스트 파일 삭제
for img_file in image_files:
    if img_file not in text_files:
        img_file_path = os.path.join(image_folder, img_file + '.jpg')
        os.remove(img_file_path)
        print(f'Deleted: {img_file_path}')

print("Cleanup completed.")
