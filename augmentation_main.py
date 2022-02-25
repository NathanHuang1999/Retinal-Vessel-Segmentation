import os, shutil
from augmentation.methods import *

def apply():
    do_augment_path = "./data/train"
    augment_path_base = "./augmentation/"

    # # rotation旋转
    # # 测试通过
    # rt_angles = [30]
    # rt_seed = 1
    # for angle in rt_angles:
    #     rt_n = augment_path_base + "rt_{degree}/".format(degree=angle)
    #     if not os.path.exists(rt_n):
    #         os.mkdir(rt_n)
    #         rotation((angle, -angle), rt_seed, do_augment_path, rt_n)
    #     else:
    #         print("Augmentation technique {method} (degree = ({dgr1}, {dgr2})) has been already done.".format(method="rotation", dgr1=angle, dgr2=-angle))
    #
    # # white_noise白噪声
    # # 测试通过
    # wn_10 = augment_path_base + "wn_10/"
    # if not os.path.exists(wn_10):
    #     os.mkdir(wn_10)
    #     apply_white_noise(do_augment_path, wn_10, [10])
    # else:
    #     print("Augmentation technique {method} has been already done.".format(method="white noise"))
    #
    # # dropout
    # # 测试通过
    # do_0_1 = augment_path_base + "do_0_1/"
    # if not os.path.exists(do_0_1):
    #     os.mkdir(do_0_1)
    #     apply_dropout(do_augment_path, do_0_1, [0.1])
    # else:
    #     print("Augmentation technique {method} has been already done.".format(method="dropout"))

    # 弹性形变
    ed_default = augment_path_base + "ed_default/"
    if not os.path.exists(ed_default):
        os.mkdir(ed_default)
        apply_elastic_deformation(do_augment_path, ed_default)
    else:
        print("Augmentation technique {method} has been already done.".format(method="elastic deformation"))


def merge_augmentations(augment_dir, output_dir, list_of_aug_files):

    os.mkdir(output_dir + '/images')
    os.mkdir(output_dir + '/labels')

    for folder in list_of_aug_files:
        if folder != 'base':
            for file in sorted(os.listdir(augment_dir + '/' + folder + '/images')):
                shutil.copy(augment_dir + '/' + folder + '/images/' + file, output_dir + '/images/' + folder + '_' + file.split('.')[0] + '.png')
                shutil.copy(augment_dir + '/' + folder + '/labels/' + file, output_dir + '/labels/' + folder + '_' + file.split('.')[0] + '.png')
                #shutil.copy(augment_dir + '/' + folder + '/images/' + file, output_dir + '/images/' + file)
                #shutil.copy(augment_dir + '/' + folder + '/labels/' + file, output_dir + '/labels/' + file)
        else:
            for file in sorted(os.listdir(augment_dir + '/' + folder + '/images')):
                shutil.copy(augment_dir + '/' + folder + '/images/' + file, output_dir + '/images/' + file.split('.')[0] + '.png')
                shutil.copy(augment_dir + '/' + folder + '/labels/' + file, output_dir + '/labels/' + file.split('.')[0] + '.png')
                #shutil.copy(augment_dir + '/' + folder + '/images/' + file, output_dir + '/images/' + file)
                #shutil.copy(augment_dir + '/' + folder + '/labels/' + file, output_dir + '/labels/' + file)

        print(folder + ' folder has been merged...')
        print('Number of images in output: ' + str(len(os.listdir(output_dir + '/images'))))
    print('Merging is done successfully!')


if __name__ == "__main__":

    apply()

    augment_dir = "./augmentation"
    if not os.path.exists(augment_dir):
        os.mkdir(augment_dir)

    merge_augmentations_path = "./data/augmentation/augment_id_1"
    if not os.path.exists(merge_augmentations_path):
      if not os.path.exists("./data/augmentation"):
        os.mkdir("./data/augmentation")
      os.mkdir(merge_augmentations_path)

    if not os.path.exists("./augmentation/train"):
        os.mkdir("./augmentation/train/")
        #os.mkdir("./augmentation/train/images/")
        #os.mkdir("./augmentation/train/labels/")
        shutil.copytree("./data/train/images/", "./augmentation/train/images/")
        shutil.copytree("./data/train/labels/", "./augmentation/train/labels/")

    augment_list = ["train", "rt_30"]

    merge_augmentations(augment_dir, merge_augmentations_path, augment_list)  



