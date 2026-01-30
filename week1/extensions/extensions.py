def main():
    filename = input("File name: ").lower().strip()
    extension = filename.split(".")[-1]

    match extension:
        case "gif" | "png":
            print("image/" + extension)
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "txt":
            print("text/plain")
        case "pdf" | "zip":
            print("application/" + extension)
        case _:
            print("application/octet-stream")


main()
