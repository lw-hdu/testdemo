import time,random

while 1:
	choice=input('是否还要开始(是/否)')
	if choice=='否':
		break
	else:
		pass

#########
	for i in range(1,4):
		print('这是第'+str(i)+'局')
		print('*****************')
		time.sleep(1)
	# 生成双方角色，并生成随机属性。
		player_life = random.randint(100,150)
		player_attack = random.randint(30,50)
		enemy_life = random.randint(100,150)
		enemy_attack = random.randint(30,50)

	# 展示双方角色的属性
		print('【玩家】\n'+'血量：'+str(player_life)+'\n攻击：'+str(player_attack))
		print('------------------------')
		time.sleep(1)
		print('【敌人】\n'+'血量：'+str(enemy_life)+'\n攻击：'+str(enemy_attack))
		print('------------------------')
		time.sleep(1)

	# 双方PK
		while player_life > 0 and enemy_life > 0:
			player_life = player_life - enemy_attack
			enemy_life = enemy_life - player_attack
			print('你发起了攻击，【敌人】剩余血量'+str(enemy_life))
			print('敌人向你发起了攻击，【玩家】剩余血量'+str(player_life))
			print('-----------------------')
			time.sleep(1.5)

	# 打印战果
		player_sorce=0
		enemy_sorce=0
		if player_life > 0 and enemy_life <= 0:
			player_sorce=player_sorce+1
			print('玩家赢')
		elif player_life <= 0 and enemy_life > 0:
			enemy_sorce=enemy_sorce+1
			print('敌人赢')
		else:
			print('平手')


	if(player_sorce>enemy_sorce):
		print('最终玩家赢')
	elif(player_sorce<enemy_sorce):
		print('最终敌人赢')
	else:
		print('最终平手')

