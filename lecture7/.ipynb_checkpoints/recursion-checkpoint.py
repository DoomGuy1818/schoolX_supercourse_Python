tree = {
    1:{
        1:{
            1: 'text',
            2: 'text',
            3: 'text',
        },
    },
    2:{
        1: {
            1: {
                1: {
                    
                    1: 'folder',
                    2: 'folder',
                    3: 'target_folder',
   
                },
                2: [1, 2, 3]
            },
        },
    },
}

def rec_find(tree: dict, name: str):
    for key, value in tree.items():
        if isinstance(value, dict):
            print(f"ключ - {key}, значение - {value}")

rec_find(tree, 'target_folder')