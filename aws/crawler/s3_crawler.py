from aws.config.s3 import S3Config
#Then use the session to get the resource

bucket_obj_list = []

class S3Crawler:
    
    @staticmethod
    def get_objects(bucket_name, target_folder=""):
        obj_dict = {target_folder:[]}
        my_bucket = S3Config.s3.Bucket(bucket_name)

        for my_bucket_object in my_bucket.objects.all():
            #bucket_obj_list.append(my_bucket_object)
            object_key = my_bucket_object.key
            #for obj in bucket_obj_list:
            if target_folder in object_key.split('/'):
                print(object_key.split('/'))
                obj_dict[target_folder].append(object_key)
            print(my_bucket_object.key)
        return obj_dict