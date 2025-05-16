from loguru import logger
import update
import downloader

print("""
你想要做些什么？输入对应功能的序号使用功能。
1.查看当前EECT程序版本
2.检查更新
3.安装已下载的更新
4.配置更新设置
5.关于EECT Update程序
exit.关闭程序\n""")



def main():
    home()


def home():
    ask = input(">")

    match ask:
        case "1":
            logger.info("查看当前EECT程序版本\n")
            print(f"当前使用的EECT版本：{update.check_version(1)}（{update.check_version(0)}）")
            main()

        case "2":
            logger.info("检查更新\n")
            print("检查更新中...")
            update_info = update.update()
            if update_info[0]:
                print(f"\n摘要：有新版本可用！")
                ask = input("是否下载更新？（y/n，默认n）：")
                if ask == "y":
                    logger.info("准备下载更新")
                    downloader.download_file(update_info[6], update_info[7], "./cache/download")
                    main()
                else:
                    main()
            else:
                print("\n摘要：当前已是最新版本。")
                main()

        case "3":
            print("未完工")
            main()

        case "4":
            print("未完工")
            main()

        case "5":
            print("""
EECT Update程序
版本: 0.0.1
版本号: 250515

一个EECT更新组件，可以快速更新EECT。

Copyright © 2025 EECT Team, All Rights Reserved.\n""")
            main()

        case "exit":
            logger.info("关闭程序\n")
            exit(0)

        case "":
            main()

        case _:
            print("    *")
            main()


if __name__ == "__main__":
    main()
