from rake import Rake

text = "Input/output (I/O), refers to the communication between an information processing system (such as a computer), " \
       "and the outside world possibly a human, or another information processing system. " \
       "Inputs are the signals or data received by the system, " \
       "and outputs are the signals or data sent from it Devices that provide " \
       "input or output to the computer are called peripherals On a typical personal computer, " \
       "peripherals include input devices like the keyboard and mouse, and output devices such as the display and printer. " \
       "Hard disk drives, floppy disk drives and optical disc drives serve as both input and output devices"

# Split text into sentences
sentenceList = split_sentences(text)
#stoppath = "FoxStoplist.txt" #Fox stoplist contains "numbers", so it will not find "natural numbers" like in Table 1.1
stoppath = "SmartStoplist.txt"  #SMART stoplist misses some of the lower-scoring keywords in Figure 1.5, which means that the top 1/3 cuts off one of the 4.0 score words in Table 1.1
stopwordpattern = build_stop_word_regex(stoppath)

# generate candidate keywords
phraseList = generate_candidate_keywords(sentenceList, stopwordpattern)

# calculate individual word scores
wordscores = calculate_word_scores(phraseList)

# generate candidate keyword scores
keywordcandidates = generate_candidate_keyword_scores(phraseList, wordscores)
if debug: print keywordcandidates

sortedKeywords = sorted(keywordcandidates.iteritems(), key=operator.itemgetter(1), reverse=True)
if debug: print sortedKeywords

totalKeywords = len(sortedKeywords)
if debug: print totalKeywords
print sortedKeywords[0:(totalKeywords )]

rake = Rake("SmartStoplist.txt")
sample_file = open("./SmartStoplist.txt",'r')
text = sample_file.read()
keywords = rake.run(text)
print keywords