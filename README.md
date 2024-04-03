安装好solanacil 安装文档 https://docs.solanalabs.com/cli/install 
安装好后创建key文件 solana-keygen new --outfile keypair.json  
然后cd orenb将ore和ore.py移到root文件夹下面
给ore执行权限chmod +x ore
然后screen 
最后启动脚本 python3 ore.py
要多地址就多创建几个密钥文件solana-keygen new --outfile keypair1.json比如这样第2个就solana-keygen new --outfile keypair2.json

然后把ore.py里面的# 设置要运行的命令
command = "./ore --keypair keypair.json --rpc https://api.mainnet-beta.solana.com mine "

keypair.json 改成对应的然后创建一个新的py脚本比如ore1.py把刚刚修改好的代码输入进去然后保存然后就是运行
