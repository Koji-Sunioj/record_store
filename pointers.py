from db import table_scan,create_album,get_album,delete_album, patch_album

options = {
    "GET":table_scan,
    "POST":create_album,
    "GET_album":get_album,
    "DELETE_album":delete_album,
    "PATCH_album":patch_album,
}

return_object = {
    "POST":{"message":"sucessfully created"},
    "GET": {},
    "GET_album":{},
    "DELETE_album":{"message":"successfully deleted"} ,
    "PATCH_album":{"message":"successfully updated"} ,
}

