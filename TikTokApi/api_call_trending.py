from TikTokApi import TikTokApi
import sys

args = sys.argv  # a list of the arguments provided (str)
scrape_nr_results, custom_verifyFp, filename = int(args[1]), str(args[2]), str(args[3])

print("scrape_nr_results:" , scrape_nr_results)
print("custom_verifyFp:" , custom_verifyFp)
print("filename:" , filename)


print("Call TikTokApi")
api = TikTokApi.get_instance()
trending = api.by_trending(count=scrape_nr_results, custom_verifyFp=custom_verifyFp)


print("Write result to file:" , filename)
import json
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(trending, f, ensure_ascii=False, indent=4)

print("Done")
