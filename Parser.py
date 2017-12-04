import vk_api
import Config
import Json


def main():

	clear_spisok = []
	
	try:
		vk_session = vk_api.VkApi(token=Config.vk_token)

		vk = vk_session.get_api()
 
		response = vk.newsfeed.search(q='#Python', count=200) 
		s = []
		for i in response['items']:
			s.append('https://vk.com/wall' + str(i['owner_id']) + '_' + str(i['id']))
			
		Json.encode_json('Spisok_postov', s)
		
	except(UnicodeEncodeError):
		pass
		
	return s

main()

