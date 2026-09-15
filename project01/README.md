# Introduction
This project parses data from a specialized ClinVar VCF file. The AF_EXAC key describes the allele frequencies and the CLNDN key gives the names of the diseases associated with it. The goal is to identify rare variants and tally the diseases linked to them. A variant is considered rare if its AF_EXAC value is below 0.0001. For each rare variant, the program extracts its associated diseases from CLNDN, splitting multiple diseases apart where needed and excluding placeholder values that don't represent real diagnoses. The program reads the file one line at a time and tallies each disease into a running dictionary, printing the final counts once the file is done.

The program is structured into three functions, each with a single responsibility. parse_line judges one line and returns its associated diseases if it's rare, update_dictionary folds those diseases into the running tally, and read_file coordinates the process, looping through the file and calling the other two.

Our group, Amanda, Mara, and Ildiko, collaborated using a GitHub fork-and-pull-request workflow, with Amanda as group leader. It was a valuable exercise in working asynchronously through GitHub, making decisions and writing code as a group, and writing a substantial amount of string operations to parse a VCF file.

All required functionality described in the assignment instructions was completed. The final program includes both required functions, read_file and parse_line, along with an additional function, update_dictionary, that the group added by choice to keep each function limited to a single responsibility. No functionality was deferred or left incomplete.

# Pseudocode

### read_file()

    # initialize empty dict
    # open file
    # loop through lines of file
        # call parse_line
        # if list not empty
            # call update_dictionary
    # return dictionary


### parse_line()
    """Takes a line from a vcf file as a string and returns a list of CLNDN 
    diseases or an empty string where applicable."""

    # initialize empty list
    # skip line if # at start
    # check for AF_EXAC
    # if AF_EXAC exists:
        # extract AF_EXAC using find function and string truncating method
        # if not significant
           # skip line
        # else
            # parse CLNDN using same method as AF_EXAC
            # separate things by pipe into separate list elements
            # drop list elements that are not_specified or not_provided
            # remove potential duplicates

    ## AF_EXAC not present
    # else:
        # skip line, return None or return empty list

    # return list


### update_dictionary()
    """Takes in dictionary and list and returns a dictionary."""
    # loop over elements in list
        # if key exists in dictionary
            # add one to value
        # else
            # initialize key with value of 1

    # return dictionary

# Results Output
Final disease count:
{'Cardiovascular_phenotype': 14,
 'Cleft_palate': 1,
 'Congenital_myasthenic_syndrome': 3,
 'Developmental_regression': 1,
 'Dystonia': 1,
 'EEG_with_generalized_epileptiform_discharges': 1,
 'Ehlers-Danlos_syndrome,_progeroid_type,_2': 2,
 'Expressive_language_delay': 1,
 'Failure_to_thrive': 1,
 'Global_developmental_delay': 2,
 'Growth_delay': 1,
 'Hypothyroidism': 1,
 'Idiopathic_generalized_epilepsy': 14,
 'Immunodeficiency_16': 2,
 'Immunodeficiency_38_with_basal_ganglia_calcification': 3,
 'Inability_to_walk': 1,
 'Inborn_genetic_diseases': 2,
 'Infantile_axial_hypotonia': 1,
 'Intellectual_disability': 1,
 'Limb_hypertonia': 1,
 'Marfanoid_habitus': 1,
 'Mental_retardation,_autosomal_dominant_42': 1,
 'Multifocal_epileptiform_discharges': 1,
 'Muscular_hypotonia': 2,
 'Myasthenic_syndrome,_congenital,_8': 79,
 'Myelodysplastic_syndrome': 1,
 'Neurodevelopmental_Disability': 2,
 'Nystagmus': 1,
 'Seizures': 2,
 'Severe_Myopia': 1,
 'Shprintzen-Goldberg_syndrome': 37,
 'Spinocerebellar_ataxia_21': 1,
 'Spondyloepimetaphyseal_dysplasia_with_joint_laxity': 1,
 'Strabismus': 1,
 'Upper_limb_hypertonia': 1,
 'hypotonia': 2}

# Evidence and Reasoning
 Amanda's implementation and Ildiko and Mara's implementation were written independently, using different internal approaches to locating AF_EXAC and to filtering header lines, yet all three produced this identical final disease count when run against the same file. This agreement between structurally different implementations serves as an informal cross-check on the correctness of the result. We did not perform additional automated testing beyond this comparison, so edge cases not represented in this particular VCF file, such as malformed INFO fields or unusual CLNDN formatting, remain unverified.

# Successes
We originally coded individually and then compared our code, and found that comparing our different approaches was one of the most useful parts of the process. Amanda's version follows the instructions very literally.  Her read_file does no filtering of its own and simply passes every line to parse_line, which then has to check for header lines, check for AF_EXAC, and handle everything else itself, making parse_line longer and more complex. Ildiko and Mara both instead had read_file filter out header lines before anything reaches parse_line, which is more efficient, but relies on read_file taking on some of the checking that the instructions describe as parse_line's job. Both approaches produce functional, correct programs. Since neither approach was wrong, working through this tradeoff, strict adherence to the assignment's described function boundaries versus overall efficiency, was a genuinely useful exercise.

A related difference came up in how each of us located AF_EXAC within a line. Amanda's parse_line searches the raw line directly for the substring AF_EXAC using Python's find function. Ildiko and Mara both first split the line into its tab-separated columns, then searched specifically within the INFO column. Comparing the two showed a similar tradeoff.  Amanda's method is more contained within a single function, while the other isolates the search to a smaller, more relevant piece of text first.

We also picked up a useful debugging habit from Amanda that proved powerful for writing correct code in a program with substantial string operations: adding a print statement after nearly every step while writing a function, so the logic can be watched working, or failing, line by line, rather than only discovering a problem after the function returns an unexpected result. Once a section is confirmed working, the print statements are commented out rather than deleted, so they remain available for troubleshooting later. This was a game changer!

On the collaboration side, our biggest success was working through Git and GitHub together as a group with mixed experience levels. Amanda walked Mara and Ildiko through forking, branches, and pull requests, and the three of us practiced the push, pull, and pull-request cycles together, successfully sharing our work throughout the project and allowing for asynchronous collaboration. This is a skill that will serve us well in our future careers as bioinformaticians.

# Struggles
One of the biggest struggles for this project was that both Ildiko and Mara were more novice Python users and were quite rusty going into this exercise, having not written Python in some time. Relearning how to code, alongside learning Git and GitHub for the first time, made for a genuinely challenging combination.  Amanda was a very gracious group leader and patient teacher, explaining the theory behind much of her more sophisticated code.

On the Git and GitHub side specifically, it took real time and repetition to get comfortable with the workflow.  Understanding the difference between a start branch and a PR branch and why both are needed to open a pull request, learning that git add alone does not save anything until git commit is run, and discovering that forks do not automatically sync with each other. A teammate's push to their own fork, or to the original repository, has to be manually pulled in before it shows up anywhere else. This caused real confusion at one point when a teammate's new file did not appear locally even though it was visible on GitHub, which turned out to be because we were looking at two different repositories, a fork and the original, that looked nearly identical.

We also ran into a smaller but instructive snag when trying to run a finished script.  A FileNotFoundError on the VCF file, which turned out to be a working-directory issue rather than a missing-file issue. Python looks for a relative filename starting from wherever the terminal is standing, not from wherever the script itself is saved, and VS Code's run button does not always use the terminal tab that is currently active. Using different IDE's did not pose any unexpected issues for the collaboration.

Even though we worked well together as a group, it took a little time to hit our stride, particularly while getting used to a new class's teaching style and expectations. Adjusting to a new platform and workflow, on top of the technical learning curve, meant our first several sessions together were as much about figuring out how to collaborate effectively as they were about the assignment itself.

# Reflection and Adaptive Learning
Each of the struggles points to a specific thing we'd do differently next time. For the repository confusion, we'd check the repository owner and URL first before assuming a git command itself was broken. For the forks-not-syncing issue, we'd build a habit of fetching from upstream at the start of every work session rather than only doing so reactively after noticing something was missing. For the FileNotFoundError, we now know to check the terminal's working directory before assuming a file is misplaced, and to run scripts directly from the terminal rather than relying on an IDE's run button, since it doesn't always use the terminal we expect. More broadly, since two of us came into this project with rusty Python and no prior Git experience, we'd budget deliberate time early on to practice the basic Git workflow, add, commit, push, pull, branch, on a low-stakes test file before touching real project code, rather than learning the mechanics for the first time under the pressure of an actual deadline.  Most of these should resolve naturally as our workflow becomes more practiced, though new technical challenges will likely surface as the projects grow more complex.

# Personal Reflections
## Group Leader:  Amanada
After attending our first lecture as a class, I realized that I may be one of the more experienced programmers here. 
I went into this project ready to take on the role as group leader, knowing how unintuitive and frustrating learning 
GitHub is. 

My first impression of the project was that it seems like a very good starting point for an algorithms course. It hits on 
so many core concepts that I learned early in my programming journey. While I have reasoned through code like this many times at
this point in my career, I have never had the opportunity to teach others how to approach these problems. It was a wonderful
experience to work with Ildiko and Mara, two bright and enthusiastic scientists like myself. I was able to teach them 
some tips I have picked up over the years that help me tackle these problems quickly and thoroughly while limiting errors along the way. 

Given that they had less experience than me, I was pleasantly surprised at how much they were able to contribute their 
to the project. Our end result is truly a comprehensive effort at solving this problem according to our interpretation of 
Dr. Sherman's instructions.

## Other member:  Ildiko
Coming into this project, I had not written Python in a while, so my first goal was simply to get comfortable writing code again. I had never written pseudocode before, and I found that starting with plain-English pseudocode before writing any real code helped a great deal, since it let me work out the logic without also fighting rusty syntax at the same time. The more organized and well-planned my pseudocode was, the easier it was to translate into actual code.

The most valuable thing I picked up from this project was Amanda's print-statement debugging habit.  Adding print statements at almost every step while writing a function, watching it process real data line by line, and only commenting them out once things worked. This made it dramatically easier to catch a mistake exactly where it happened, rather than getting a wrong final answer and working backward to find out why. It saved so much time troubleshooting bad code. I plan to use this consistently going forward, especially while my Python is still rusty.

Overall, I really enjoyed working with Amanda and Mara. Amanda has more experience with both Python and GitHub, and she was a patient, thorough teacher rather than someone who just handed us answers. It was helpful being on a similar level as Mara and we worked together to troubleshoot and learn independently in parts, as we often had similar questions and struggles.  When our approaches diverged, whether in code design or in how to interpret the instructions, we talked it through as a group, asked each other real questions, and reached a shared decision rather than any one person deciding for the group. That collaborative problem-solving was, honestly, the best part of this project.

## Other member:  Mara
The operations performed in this project not only have real-life use-cases but was very beneficial for reinforcing some core concepts about string manipulation. Additionally, learning GitHub, which I'd never previously used, will be useful moving forward.  
 
I found writing pseudocode in plain English to be a very practical skill. I have not had much experience writing it and tended to also include lines of code while formatting my ideas, so keeping the format consistent made writing the actual code easier. Additionally, seeing Amanda use print statements to check lines of code is a great idea, and one that I will be using moving forward. I'd been taught that more print statements was a good idea, but I hadn't seen it in practice before. 
 
Amanda was an excellent group leader and was very patient with both me and Ildiko working through our code and learning GitHub and had an in-depth explanation for every question asked. Ildiko and I, having similar Python experience, were able to talk each other through our various knowledge gaps, and effectively communicate any shared coding uncertainties. I found it very valuable to learn to work collaboratively in a remote environment.  

# Data Source
Landrum MJ, Lee JM, Riley GR, Jang W, Rubinstein WS, Church DM, Maglott DR. ClinVar: public archive of relationships among sequence variation and human phenotype. Nucleic Acids Research. 2014;42(1):D980–D985. doi:10.1093/nar/gkt1113.

# Generative AI Appendix
Generative AI was used to generate the ClinVar citation.
