def main():
    # no_of_words = int(raw_input())
    # list_of_words = []
    # list_of_matching_words = []
    # dictonary_formed = []
    # for i in range(no_of_words):
    #     list_of_words[i] = raw_input()
    
    
    # for j in range(no_of_words):
    #     word_formed = lower(list_of_words[j])
    #     for k in range(97,123):
    #         if ord(word_formed[i]) == k :
                

 # Write code here 
    no_of_words = int(raw_input())
    list_of_words = [0 for x in range(no_of_words)]
    for i in range(no_of_words):
        list_of_words[i] = raw_input()
    
    new_list = sorted(list_of_words)
    
    for i in range(0,len(new_list)):
        print new_list[i]

main()

