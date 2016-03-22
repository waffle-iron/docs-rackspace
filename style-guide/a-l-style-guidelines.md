# A-L style reference

This section of the writing style guide provides detailed guidelines about and instructions for applying style conventions. For more guidelines, see [M-Z style reference](m-z-style-guidelines.md).

- [Acronyms and other abbreviations](#acronyms)
- [Capitalization](#capitalization)
- [Citations](#citations)
- [Cloud account information](#cloud-account-info)
- [Code examples](#code-examples)
- [Contractions](#contractions)
- [Copyrights](#copyrights)
- [Dates](#dates)
- [Email addresses](#email-addresses)
- [File types](#file-types)
- [Glossaries](#glossaries-section)
- [IP addresses](#ip-addresses)
- [Keyboard keys](#keyboard-keys)
- [Links and cross-references](#links)
- [Lists](#lists-1)

## <a name="acronyms"></a>Acronyms and other abbreviations
Unless an abbreviation is common, spell out the root words of the abbreviation on the first use in an article or topic. Show the abbreviation in parentheses after the spelled-out term. On subsequent uses in the article or topic, use the abbreviation. If you introduce an abbreviation, use it; do not alternate between the abbreviation and the spelled-out term.

**Note:** In FAQ documents, users will likely skip directly to a specific Q&A pair and therefore might miss the spelling out of an abbreviation earlier in the FAQ. Follow the preceding guideline for each Q&A pair, which might result in spelling out a term and introducing the abbreviation several times within one FAQ document.

Do not capitalize the spelled-out term unless it is a proper name or normally capitalized. For example, the spelled-out term for *AJAX* is *Asynchronous JavaScript and XML*, but the spelled-out term for *ACL* is *access control list*.

Occurrence | Use | Do not use
--- | --- | ---
First	| access control list (ACL) | ACL <br /> ACL (access control list) <br /> ACL (Access Control List) <br /> Access Control List (ACL)
Subsequent	| ACL	| access control list
First	| OS	| operating system (OS)

Also use the following guidelines related to abbreviations.

Guideline | Use | Do not use
--- | --- | ---
In titles and headings, do *not* show both the spelled-out term and its abbreviation. In most cases, you can use the abbreviation in the title or heading and show the spelled-out term and its abbreviation on first use in the text. | **Adding an ACL** <br /> <br /> An access control list (ACL) allows access from an outside network into the ObjectRocket system. | **Adding an access control list (ACL)** <br /> <br /> An ACL allows access from an outside network into the ObjectRocket system.
Use only established abbreviations. Do not create new ones. |	hybrid cloud |	HC
Do not use abbreviated forms of Rackspace product names. <br /><br /> However, if you think that a customer might use an abbreviated name in a search, you can tag the document with the abbreviation. | Cloud Block Storage |	CBS
Use the indefinite article (*a* or *an*) that is appropriate with the pronunciation of the abbreviation. For example, the abbreviation of *Structured Query Language (SQL)* is pronounced "es-cue-el" and takes the article *an*. *SQL* in the Microsoft product name *SQL Server* is pronounced "sequel" and takes the article *a*. | an SDK <br /><br /> a SQL Server instance | a SDK <br /><br /> an SQL Server instance
If an abbreviation is used as part of a compound modifier, hyphenate it as you would a word. | 1000-bps rate |	1000 bps rate
Do not surround abbreviations with quotation marks. |	OS	| "OS"
Use periods only if the abbreviation normally has them (for example, *a.m.* and *p.m.*) or could otherwise be misread as a word, such as *in.* (for *inch*).	| FAQ	| F.A.Q.
Do not use an abbreviation as a verb.	| Use FTP to copy the file to the server.	| FTP the file to the server.
Avoid using abbreviations in the possessive. Instead, treat the abbreviation as an adjective or put it in a prepositional phrase.	| Type the DBA password. <br /><br /> Type the password of the DBA. | Type the DBA's password.
To form the plural of an abbreviation, except for a unit of measure, append a lowercase *s* without an apostrophe. <br /><br /> For most abbreviations of units of measure, the singular and plural forms are the same (for example, 1 pt and 10 pt). <br /><br /> If an acronym already represents a plural noun, do not add an *s*. <br /><br /> **Note:** To refer to more than one FAQ document or section, add the appropriate noun after *FAQ* and make the noun plural—for example, *FAQ articles*. Follow this guideline for other plural acronyms when you need to refer to more than one instance of them. | user IDs <br /><br /> 10 mm <br /><br /> FAQ | user ID's <br /><br /> 10 mms <br /><br /> FAQs
For abbreviated units of measure, insert a space between the number and the abbreviation. |	256 MB	| 256MB
Do not use Latin abbreviations or non-English words and phrases. For more information, see  [Avoid obscure non-English words and abbreviations](basic-writing-guidelines.md#avoid-obscure-words).	| for example	| e.g.

### <a name="bit-byte"></a>Abbreviations of byte and bit
*Byte* is abbreviated with an uppercase *B*. *Bit* is abbreviated with a lowercase *b*. For example, *gigabyte* is abbreviated as *GB*, and *gigabit* is abbreviated as *Gb*. In general, use such abbreviations only with a number value; otherwise, spell out the term. If you want to emphasize *bit* or *byte*, use the spelled-out term rather than or in addition to the abbreviation.

| Examples |
| --- |
| The 100 GB drive appears as 107.4 GB because of how the megabytes are counted. |
| The unit of value for this alarm is megabits per second (Mbps). |

### <a name="common-abbreviations"></a>Common abbreviations
A common abbreviation is either an industry-standard abbreviation or one that is well known to the target audience for the product or service that you are documenting. Following are some common abbreviations in the computer industry. You do not need to spell out these terms on first use, unless you think the abbreviation is unfamiliar to your particular audience.

API, ASCII, BIOS, CD, CD-ROM, CGI, CLI, CPU, CSS, DNS, DVD, FAQ, FTP, GB, GHz, GUI, GUID, HTML, HTTP, HTTPS, ID, IMAP, I/O, IP, JSON, KB, kHz, LAN, LDAP, MB, MHz, NIC, NTFS, OLE, OS, PDF, PHP, POP, RAM, REST, ROM, SGML, SMTP, SQL, SSL, TCP, TCP/IP, URI, URL, USB, VLAN, WAN, XML

## <a name="capitalization"></a>Capitalization
Be judicious and consistent in your use of capitalization. Use capitalization for proper names and proper adjectives and when it is stylistically required. Do not use it for common nouns, for emphasis, to attempt to give a word greater status than other words, or randomly. This topic provides capitalization guidelines for the following items:

- [Terms](#cap-terms)
- [Code](#cap-code)
- [Variables and placeholders](#cap-variables)
- [Titles and headings](#cap-titles)
- [Lists](#cap-lists)
- [Tables](#cap-tables)
- [Glossaries](#cap-glossaries)
- [Figures](#cap-figures)
- [Capitalization with punctuation](#cap-with-punctuation)

### <a name="cap-terms"></a>Terms
Use the following guidelines to help you decide whether a word should be capitalized.
For the correct capitalization of some common terms, see [Terminology](terminology-guidelines.md).

- [Capitalize proper nouns and adjectives](#cap-proper-nouns)
- [Capitalize most acronyms, initialisms, and short forms of names](#cap-acronyms)
- [Capitalize interface labels as they are capitalized on the interface](#cap-ui-labels)
- [Capitalize the names of major components, systems, or utilities associated with a product](#cap-major-components)
- [Do not capitalize common nouns](#no-cap-common-nouns)
- [Do not use all capitals for emphasis](#no-cap-emphasis)

#### <a name="cap-proper-nouns"></a>Capitalize proper nouns and adjectives
Proper nouns and adjectives include the names of people, places, companies, organizations, products, languages, protocols, and some technologies, as well as trademarks.

Be aware that some of these names might have nonstandard or no capitalization. You should always follow the capitalization that is used by the company, shown in a dictionary, or accepted as standard in the industry.

Examples |  
--- | ---
Rackspace | Service Advertising Protocol
Hong Kong | WordPress
Fanatical Support | Boolean
Cloud Servers | OpenStack
Linux | Internet
Microsoft Windows | Ethernet
SQL Server | Wi-Fi
PuTTY | lighttpd

For the correct capitalization of Rackspace product names, see the [Rackspace Cloud corporate website](https://www.rackspace.com/cloud).

For the correct capitalization of some commonly used third-party names, see [Third-party names and trademarks](terminology-guidelines.md#third-party-terms).

#### <a name="cap-acronyms"></a>Capitalize most acronyms, initialisms, and short forms of names
Most abbreviated forms of terms use all capitals, although exceptions exist. Also, be aware that the corresponding spelled-out terms of abbreviations are often not capitalized. When in doubt about the capitalization of an abbreviation or its spelled-out term, consult a dictionary, industry style guide, reputable website, or editor. Following are some examples.

Abbreviation	| Spelled out term
--- | ---
API | application programming interface
GB | gigabyte
GHz | gigahertz
I/O | input/output
JSON | JavaScript Object Notation
Kbps | kilobits per second
REST | Representational State Transfer
SaaS | software as a service
SOA | service-oriented architecture
WSDL | Web Services Description Language

For more information about abbreviations, see [Acronyms and other abbreviations](#acronyms).

#### <a name="cap-ui-labels"></a>Capitalize interface labels as they are capitalized on the interface
When you are documenting part of the interface within a procedure or other type of article or topic, match the capitalization used on the interface.

However, when you use terms from the interface as common nouns, do not capitalize the terms.

| Use |
| --- |
| Click the action cog to the left of the check name and select **Rename Check**. |
| From the Cloud Control Panel, you can rename a check. |

#### <a name="cap-major-components"></a>Generally, capitalize the names of major components, systems, or utilities associated with a product
Follow the capitalization of major component names that is established by Marketing, Legal, and the product teams. However, be wary of overcapitalization of product terms. Not every feature or object in a product is a proper noun. For example, the Cloud Servers service enables users to create a *server*, not a *Server*. When the user creates a server, the user specifies an *image*, *flavor*, and *network*, not an *Image*, *Flavor*, and *Network*. A Performance server has a *data disk* and a *system disk*, not a *Data disk* and a *System disk*. A customer uses Cloud Load Balancer to create a *load balancer*, not a *Load Balancer*.

Many terms that might be capitalized on the interface are not capitalized when used as common nouns. When in doubt, consult an existing style sheet, an editor, or the product team (but be aware that product teams sometimes tend to overcapitalize terms). Following are some tips to help you determine whether a noun should be capitalized:

- Generally, if you can have more than one of something, it is a common noun and therefore not capitalized.
- When a common noun follows the name of a product or component, generally that noun is not capitalized.
- When you refer generally to a component, you can use lowercase (as in the utility or the agent).

| Examples |
| --- |
| Cloud Control Panel |
| Zipit Backup Utility |
| Rate Limiting component |
| Cloud Identity service |
| servers |
| backups |
| containers |
| authentication |

#### <a name="no-cap-common-nouns"></a>Do not capitalize common nouns
Most of the time, we have no trouble determining whether a noun is proper or common. However, there is a tendency to capitalize product-specific terms even when they are really just being used as common nouns. A common noun denotes a whole class of something (for example, *servers*) or a random member of a class (for example, *a server*). As a general rule, if you can have more than one of something, it is a common noun and therefore not capitalized.

Use | Do not use
--- | ---
You can submit up to 10 messages in a single request, but you must encapsulate them in a collection container (an array in JSON). | You can submit up to 10 Messages in a single Request, but you must encapsulate them in a Collection Container (an Array in JSON).
Repose authentication provides caching for user tokens, roles, and groups. |	Repose Authentication provides caching for User Tokens, Roles, and Groups.

#### <a name="no-cap-emphasis"></a>Do not use all capitals for emphasis
To emphasize a term, show it in italics. To emphasize an important piece of information, consider setting it apart structurally, perhaps as a note.

### <a name="cap-code"></a>Code
If you are showing sample code, follow the conventions of the programming language used and preserve the capitalization that the author of the code used.

### <a name="cap-variables"></a>Variables and placeholders
Use camelCase (for example, *userName*) unless you have to follow the conventions of the programming language. For example, you might need to use underscores (*user_name*) or all capitals (*USER_NAME*).
For more information about formatting placeholders, see [Text formatting](m-z-style-guidelines.md#text-formatting).  

### <a name="cap-titles"></a>Titles and headings
Use [sentence-style capitalization](#cap-sentence-style) for most titles and headings, including article, chapter, table, figure, and example titles, as well as section and procedure headings. One exception is book titles, which use [title-style capitalization](#cap-title-style).

For additional guidelines for titles and headings, see [Titles and headings](m-z-style-guidelines.md#titles-headings).

#### <a name="cap-sentence-style"></a>Guidelines for sentence-style capitalization
In sentence-style capitalization, you capitalize only the first word of the title or heading, plus any proper nouns, proper adjectives, and terms that are always capitalized, such as some acronyms and abbreviations. If the title includes a colon, capitalize the first word that follows the colon, regardless of its part of speech.

If the heading includes text from a user interface, the capitalization of that text must match the capitalization on the interface.

| Examples |
| --- | --- |
| Preparing a cloud server to be a mail server | Can I buy extra IP addresses?|
| What are cloud servers? | What are the PHP configuration limits for Cloud Sites? |
| Install or upgrade PHP 5.3 for CentOS 5.x | How do I install my own PEAR module?|
| Ubuntu Hardy: Using mod_python to serve your application | I live outside the United States. Can I use my foreign credit card to pay for my account?|
| Shopping cart software: The basics | Troubleshooting a Vyatta site-to-site VPN connection |
| Back up your files | Differences between IMAP and POP |

#### <a name="cap-title-style"></a>Guidelines for title-style capitalization
Title-style capitalization uses initial uppercase letters for the first, last, and all the significant words in the title.

Capitalize all words in the title except for the following types of words:
- Articles (*a*, *an*, *the*) unless the article is the first word in the title or follows a colon
- Coordinating conjunctions (*and*, *but*, *for*, *nor*, *or*, *yet*, *so*) unless the conjunction is the first word in the title
- Prepositions of any length, unless the preposition is the first or the last word in the title or is part of a verb phrase
- The word *to* in an infinitive phrase unless to is the first word in the title
- Second elements attached by hyphens to prefixes unless they are proper nouns or proper adjectives
- Words that always begin with a lowercase letter, such as literal command names or certain product or software names

| Examples |
|---|
| Next Generation Cloud Servers Developer Guide |
| Rackspace Cloud DNS Getting Started Guide |
| Cloud Files Introduction |
| Cloud Networks Release Notes |
| API Writers Guide |

### <a name="cap-lists"></a>Lists
Capitalize the first letter of each list item unless the first letter must be lowercase.

For additional guidelines about formatting lists, see [Lists](#lists-1).

### <a name="cap-tables"></a>Tables
Use [sentence-style capitalization](#cap-sentence-style) for table titles, column headers, row headers, and text in table cells.

### <a name="cap-glossaries"></a>Glossaries
Use the following guidelines for capitalizing terms and definitions in glossaries:
- For the glossary term, use lowercase letters unless the term is a proper noun or acronym. For example, use *server* instead of *Server*.
- For the definition, use [sentence-style capitalization](#cap-sentence-style).

| Example |
| --- |
| **token** <br /> An opaque string that represents an authorization to access cloud resources. Tokens might be revoked at any time and are valid for a finite duration. |

For more information about formatting glossary entries and definitions, see [Glossaries](a-l-style-guidelines.md#glossaries).

### <a name="cap-figures"></a>Figures
Use [sentence-style capitalization](#cap-sentence-style) for figure titles, text callouts within figures, and for legends associated with a figure.

### <a name="cap-with-punctuation"></a>Capitalization with punctuation
Always capitalize the first word of a new sentence. Do not start a sentence with a case-sensitive lowercase word (such as a lowercase command name).

Do not capitalize the word that follows a colon in a sentence, unless the word is proper or is the beginning of a quotation.

Do not capitalize the word following an em dash, unless the word is proper.

## <a name="citations"></a>Citations

Occasionally you might want to include content from a third-party source. If you do so, you must ensure that the source is reputable, the information is accurate, the quoted material is distinguished from the surrounding content, and the source is cited. Follow these guidelines:

- Include content only from expert sources that have a named author or are from a known company. Do not quote Wikipedia articles.
- If necessary, verify that the content is accurate.
- Set off the quoted content from the other content in the following ways:
  - If the quotation is short (just a phrase or sentence), you can include it in an existing paragraph. Set the quotation off with quotation marks, and put ending punctuation within the closing quotation mark.
  - If the quotation is longer than a phrase or sentence, or it makes sense to separate it from the surrounding content, you can place it in its own paragraph. Indent the paragraph to set it off from the surrounding paragraphs.
  - Do not use italics or bold to distinguish quoted content. Use such formatting only if it was used in the source.
- Attribute the source as follows:
  - If you have just one or two quotations, you can attribute them within the article text by stating the author, the source document, or both and providing a link to the source. Usually such an attribution would precede the quotation, as an introduction to it.
  - If you have more than one or two quotations, follow each quotation with a number in square brackets. Start at [1] and number each quotation in the document consecutively. At the end of the document, use a numbered list to list each resource in the order that it is shown in the article. Cite the author, the name of the source, and provide a link to the source. Put the list under a heading such as “Numbered citations in this article.” Then, go back to each numbered reference in the article and create a link between the reference number (such as [1]) and the numbered item at the end of the article.  

## <a name="cloud-account-info"></a>Cloud account information
In examples of API authentication requests, and other examples where we are teaching the use of the API and expect that users might copy the code and use it, use variables or the following standard values for account numbers, user names, passwords, API keys, and so on. Format the variables by using camelCase and italics, and also use bold within the examples.  

Information | Use | Do not use
---|---|---
Account or tenant ID	| ***yourAccountId*** <br /> ***yourTenantId*** <br /> $account <br /> $tenant | 658405
User name	| ***yourUserName***  <br /> $username | dian4554
Password	| ***yourPassword*** <br /> $password | J$123bb*
API key	| ***yourApiKey*** <br /> $apikey | kf938gf4915e114f7ff5448910ffe68c
Authentication token | ***xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx*** <br /> $token | 2e356864f39831523c184fc646b1997b

In example API operation requests and responses, in which we want users to see actual values from the system, use "real-looking" values that are nevertheless obviously made up, such the following one for `X-Auth-Token`:

`abcdef123ghi4j5k67m8910n12op3qrs`

**Warning:** Do not include or show actual writer or user account credentials in code examples or screenshots.

## <a name="code-examples"></a>Code examples
Observe the following guidelines when creating blocks of code as input or output examples:

- Do not use screenshots to show code examples. Format them as blocks of code by using the appropriate markup in your authoring tool. For more information about formatting, see [Text formatting](m-z-style-guidelines.md#text-formatting).

- When showing input, always include a command prompt (such as $).

- As often as necessary, show input and output in separate blocks and provide explanations for each. For example, if the input contains arguments or parameters, explain those. If the user should expect something specific in the output, or you want to show only part of lengthy output, provide an explanation. Provide your users the information that they need, and separate the input and output when it makes sense.

- When the command is simple, and there is nothing specific to say about the output, you can show the input and output in the same code block, as the user would actually see the code in their own terminal. The inclusion of the command prompt will differentiate the input from the output.

- Ensure that any placeholder text in code is obvious. If the authoring tool allows it, apply italics to placeholders; if not, enclose them in angle brackets. For more information about placeholders and formatting them, see [Placeholder (variable) text](m-z-style-guidelines.md#placeholders) and [Cloud account information](#cloud-account-info).

- Follow the conventions of the programming language used and preserve the capitalization that the author of the code used.

- For readability, you can break up long lines of input into readable blocks by ending each line with a backslash.

- If the input includes a list of arguments or parameters, show the important or relevant ones first, and group related ones. If no other order makes sense, use alphabetical order. If you explain the arguments or parameters in text, show them in the same order that they appear in the code block.

The following examples illustrates many many of these guidelines:

#### Create a VM running a Docker host
1. Show all the available virtual machines (VMs) that are running Docker.

    `$ docker-machine ls`

  If you have not created any VMs yet, your output should look as follows:

    `NAME   ACTIVE   DRIVER   STATE   URL`

2. Create a VM that is running Docker.

    `$ docker-machine create --driver virtualbox test`

  The `--driver` flag indicates what type of driver the machine will run on. In this case, `virtualbox` indicates that the driver is Oracle VirtualBox. The final argument in the command gives the VM a name, in this case, `test`.

  The output should as follows:
    ```
    Creating VirtualBox VM...
    Creating SSH key...
    Starting VirtualBox VM...
    Starting VM...
    To see how to connect Docker to this machine, run: docker-machine env test
    ```
3. Run docker-machine ls again to see the VM that you created. <br />
The output should look as follows:
    ```
    NAME             ACTIVE   DRIVER       STATE     URL                         SWARM
    test                      virtualbox   Running   tcp://192.168.99.101:237
    ```

#### Run the application
1. Run a container from the image. The application code uses the environment variables that you defined to connect to the MongoDB container.
    ```
    $ docker run --detach \
      --env MONGO_HOST=$MONGO_HOST \
      --env MONGO_PORT=$MONGO_PORT \
      --env MONGO_SSL=$MONGO_SSL \
      --env MONGO_DATABASE=$MONGO_DATABASE \
      --env MONGO_USER=$MONGO_USER \
      --env MONGO_PASSWORD=$MONGO_PASSWORD \
      --publish 5000:5000 \
      guestbook-mongo:1.0
      ```
2. View the status of the container by using the `--latest` parameter.

    `$ docker ps --latest`

  The status of the container should begin with `Up`.

#### Remove the containers already using the port
1. To identify the containers that are using the port, run the following command, changing ``<port>`` to the port number that you want to use.

    `$ docker ps -a | grep <port>/tcp`

2. To remove the containers, run the following command for each container identified in step 1, changing ``<containerId>`` to the ID of the container. <br /> The `--force` argument ensures that the container is removed even if it is currently running.

    `docker rm --force --volumes <containerId>`

#### Troubleshooting
Sometimes, when you use a docker command, you receive the following output:

    $ docker info
    Get http:///var/run/docker.sock/v1.20/info: dial unix /var/run/docker.sock: no such file or directory.
    * Are you trying to connect to a TLS-enabled daemon without TLS?
    * Is your docker daemon up and running?

If you receive this output, your VM is not running on a Docker host.

## <a name="contractions"></a>Contractions
Contractions help to create a less formal tone in documentation. Common contractions, such as *can’t* and *don’t*, are usually recognizable by readers who are proficient in English, and such contractions do not pose a problem for human translators. In general, you can use the following common contractions in content where contractions are acceptable:

- Contractions that include the word *not*, such as *aren’t*, *can’t*, *didn’t*, *doesn’t*, *don’t*, *isn’t*, *wasn’t*, *weren’t*, *won’t*, and *wouldn’t* <br /> If you want to emphasize the negative, however, do *not* use such a contraction.

- Contractions that include *is* or *are*, such as *it’s*, *that’s*, *there’s*, *they’re*, and *you’re* <br /> Because such contractions can be confused with possessives, ensure that your usage is correct.

Avoid the following types of contractions, which are not common or can be confusing depending on context:

- Contractions that can be misread as other words, such as *let’s*
- Contractions with the interrogative words *how*, *what*, *when*, *where*, *who*, and *why*
- Nonstandard or obscure contractions, such as *mustn’t*, *mightn’t*, *should’ve*, *could’ve*, and *that’ll*
- Contractions that combine a noun and a verb, such as in “The service’ll stop automatically”
- Contractions that include a company name, product name, or trademark, such as in “Rackspace’s the leader in hybrid cloud”

Use contractions consistently. Avoid mixing common contractions and spelled-out forms within the same article or set of related articles.

## <a name="copyrights"></a>Copyrights
For both API and How-To content, copyright statements are automatically inserted by the system. Use the generated statement unless RackLaw gives you other instructions.

## <a name="dates"></a>Dates
Dates are displayed differently in different countries, so you must use a date format that is explicit and consistent and that global customers cannot misinterpret.

Unless space is limited, always show dates in the following format: *month day*, *year*. Always spell out the month.

Use | Avoid
--- | ---
November 12, 2010 | 12 Nov 2010 <br /> 2010-Nov-12 <br /> 12/11/10 <br /> 11/12/10 <br /> 10-11-12

**Note:** Do not use ordinal numbers for dates. For example, do not use *January 1st*; use *January 1* instead.

When the month, day, and year are embedded in a sentence, use a comma before and after the year. When only the month and year are embedded in a sentence, omit the commas unless the syntax would ordinarily require a comma following the year.

| Use |
| --- |
| Any sites that are using MySQL 4 after November 1, 2011, will be automatically migrated to MySQL 5. |
| The Alert Logic Security Research Team used 12 months of security event data captured from July 2010 through June 2011. |
| As of September 2013, a subset of customer accounts were not being billed for actual usage in comparison to their preselected SQL Server storage allocations. |

Use an all-numeric date only in the following situations:
- Space is limited, as in a table or figure.
- You need to show a literal representation of the date as it is displayed in the software.

Because all-numeric dates are interpreted differently in different countries, explain the format of a numeric date, and use a consistent format throughout the  documentation. If possible, use the ISO 8601 format, which is *yyyy*-*mm*-*dd* (for example, 2012-11-10 for November 10, 2012).

| Use |
| --- |
| The value that is shown for 8/19/10 represents the average number of extents from data collections beginning August 19, 2010. |

## <a name="email-addresses"></a>Email addresses
For example email addresses, use **example.com** or **example.org**. The Internet Assigned Numbers Authority (IANA) reserves these domain names for use in examples.

**Note:** For How-To articles, do not use **kcexample.com**. Rackspace no longer owns this domain name. Use **example.com** or **example.org** instead.

Format example email addresses as bold. For example, **yourName@example.com**.

If you document an actual email address, use the convention in your authoring environment to make the email address live.

## <a name="file-types"></a>File types

For references to a file type in text (not code), use one of the following naming conventions, depending on the type of file and the context:

- Generic name, such as an initialization file or a configuration file
- Standard abbreviation, such as a PDF file or an XML file
- File name extension, such as a .zip file

Use a generic name or a standard abbreviation if one exists. If a generic name or a standard abbreviation does not exist or is not appropriate given the context, use the file name extension. The following table provides some common file types and guidelines for referring to them.

File type | Guideline | Example
--- | --- | ---
configuration |	Use the term *configuration* unless you are naming a specific file.	| The main logrotate configuration file is located at `/etc/logrotate.conf.`
HTML | 	Use the term *HTML* unless you are naming a specific file. | From the website, you can access HTML files. <br /><br /> The frequently asked questions are located in the **faq.htm** file.
initialization | 	Use the term *initialization* unless you are naming a specific file.	| The initialization files contain default parameter values.<br /><br />Copy the **calibrate.ini** file.
JSON	| Use the term *JSON* unless you are naming a specific file. | You can directly edit the JSON environment file to add attributes specific to your configuration. <br /><br /> The parameters provided with `/type=install` are visible in the **bootstrap.json** file.
XML |	Use the term *XML* unless you are naming a specific file.	| The file is an XML document that defines configuration information regarding the web application. <br /><br /> A service name maps to a collection of configuration entries in the Hadoop **core-site.xml** file.
zip |	Use the term *zip* for both general and specific references. | In the example, **file.zip** is the name that you assign to the zip file.

## <a name="glossaries-section"></a>Glossaries
Create a glossary to document the following items:

- New, unfamiliar, or unique terms
- Familiar terms used in a new or special way
- Abbreviations or acronyms that should be clarified

This section provides guidelines for the following items:
- [Glossary terms](#glossary-terms)
- [Glossary definitions](#glossary-definitions)
- [Cross-references to glossary terms](#glossary-xref)
- [Guidelines for a comprehensive glossary](#glossary-comprehensive)

### <a name="glossary-terms"></a>Glossary terms
To show the glossary term that you are defining, use the following guidelines:
- Use the singular form unless the term is always plural. For example, use *server* instead of *servers*.
- Use lowercase letters unless the term is a proper noun or acronym. For example, use *server* instead of *Server*.
- If the term has an acronym or abbreviation, show the term either in its spelled-out form or shortened form, depending on which term is more familiar to users. If you use the spelled-out form, follow it with the abbreviation in parentheses.

To alphabetize glossary terms, use the word-by-word method. In this method, terms that contain more than one word separated by spaces or commas are alphabetized by the first word only, unless the first word of two or more entries is the same. In that case, the second and subsequent words are used to determine the alphabetical order. Hyphens, slashes, and apostrophes continue a single word.

| Example word-by-word alphabetization |
| ---|
| new math <br /> newborn <br /> new/old <br /> newspaper |

### <a name="glossary-definitions"></a>Glossary definitions
Make your glossary definitions brief. Try to restrict definitions to no more than one or two short paragraphs, and avoid the inclusion of notes or tips. If your definition is longer than one or two short paragraphs, it might be more appropriate as a concept in an overview section rather than in a glossary.

Begin the definition with a descriptive phrase. Capitalize the first letter of the phrase, and end the phrase with a period. Follow the initial phrase with one or more sentences as needed.

How you begin the definition also depends on what part of speech the term is:

- Noun&mdash;Begin with the appropriate article (a, an, or the) and a noun phrase.
- Verb&mdash;Begin with the infinitive form of another verb that defines the term.
- Adjective&mdash;Begin with a verb such as describes or pertains to.
- Abbreviation&mdash;Begin with the spelled-out term.

The following table shows examples.

**Note:** In a comprehensive glossary, you might need to start the definition with a qualifier that identifies the service to which the term relates. For more information, see [Guidelines for a comprehensive glossary](#glossary-comprehensive).

Type | Example
--- | ---
Noun	| **token** <br /> An opaque string that represents an authorization to access cloud resources. Tokens might be revoked at any time and are valid for a finite duration.
Verb	| **resize** <br /> To convert an existing server to a different flavor, in essence, scaling the server up or down. The original server is saved for a period of time to allow rollback if a problem occurs.
Adjective	| **RESTful** <br /> Describes a kind of web service API that uses REST.
Abbreviation	| **API** <br /> Application Programming Interface. A set of commands, functions, and protocols that programmers can use to create application services by using an open application.

### <a name="glossary-xref"></a>Cross-references to glossary terms
Use the following guidelines when creating cross-references within a glossary:

- For a term with a definition located under a different entry, use a *See* entry in place of the definition.

- For a term with a definition that is related to, is similar to, or contrasts with another term, refer to the term in one of the following ways. If that term actually occurs in the definition, you can simply link to its definition from the term. If the term does not occur in the definition, add a *See also* entry at the end of the definition. <br /><br />
  **Tip:** To highlight a difference between two terms, you can use a *Contrast with* entry.

- Format the cross-reference as follows:
  - If using a *See* or *See also* reference, type *See* or *See also*, and apply italics. If you are referring to more than one item, italicize *and*.

  - Make the term a link to the cross-referenced term.

| Examples |
| --- |
| **address** <br /> See <u>address space</u>. |
| **collection** <br /> A group of <u>packages</u> that have the same <u>qualifier</u>. |
| **data point** <br /> A value that stores metrics. Metrics are stored as full resolution data points, which are periodically rolled up (condensed) into coarser data points. *See also* <u>data granularity</u>. |
| **replace** <br /> To recover by dropping the selected database and re-creating it. *Contrast with* <u>copy over</u>. |

### <a name="glossary-comprehensive"></a>Guidelines for a comprehensive glossary
A comprehensive glossary might have the following types of terms:

- Industry-standard terms
- Third-party product terms
- Rackspace-specific terms that apply to only one service
- Rackspace-specific terms that are general or apply to many different services
- Rackspace-specific terms that apply to two or more services and have different meanings for two or more services

Following are guidelines for how to handle each type of term in the comprehensive glossary:

- Include industry-standard terms only if they are integral to understanding how a Rackspace service works. However, do not include terms that are well-known or common (such as *browser* and *blog*). In the definition, describe how Rackspace incorporates the idea represented by the term, or which service employs it. For example, *API*.

- Avoid including third-party terms. Within the documentation itself, provide links to third-party websites if you want to provide more information about third-party terms. A Rackspace glossary should contain mainly Rackspace terms. If the user could find the meaning outside of a Rackspace document by using a browser search, then we probably don’t need to include it in the glossary. For example, *Apache*.

- If a term is specific to one Rackspace service, start the definition with the name of that service in parentheses, and italicize it.

- If a term is general or applies to many different services, you do not need to qualify it.

- If a term is specific to more than one service but has a different meaning for each service, provide all the relevant definitions in one glossary entry. Place each definition in a separate paragraph and start the definition with the service name, in parentheses and italicized.

## <a name="ip-addresses"></a>IP addresses
An *IP address* uses a sequence of numbers to uniquely identify a particular computer on the Internet.

When you are discussing IP addresses or referring to a specific IP address, do not use *IP* only; use *IP address*. You do not need to spell out *IP* on first use.  

When you need to refer to a specific version of the IP, use *IPv4 address* or *IPv6 address* as appropriate.

| Examples |
| --- |
| If your website is hosted in the DFW data center, you can use the following primary and secondary IP addresses: <br /> &#149; Primary: 74.205.61.228 <br /> &#149; Secondary: 74.205.61.229 <br /> &#149; Additional: 72.32.36.144/28 (72.32.36.145 - 72.32.36.158) |
| Each Vyatta appliance is assigned one public IPv4 address. |
| If you are using IPv6 on your server, you might need to add the IPv6 addresses of your name servers to the **resolv.conf** file. |

If you need to show an example IP address, do not use one that is or might be assigned to a computer. Instead, use one that is globally defined for documentation. Valid IPv4 address blocks are provided in [RFC5737](https://tools.ietf.org/html/rfc5737), and a valid IPv6 prefix is provided in [RFC 3849](http://tools.ietf.org/html/rfc3849).

## <a name="keyboard-keys"></a>Keyboard keys
Different keyboards use different names for common keys. For consistency, use the following key names unless the technology that you are documenting requires other forms:

- Alt
- arrow keys (generic)
- Backspace
- Command
- Ctrl
- Del
- Down Arrow
- End
- Enter
- Esc
- Home
- Ins
- Left Arrow
- Option
- Page Down
- Page Up
- Right Arrow
- Shift
- Space
- Tab
- Up Arrow

When showing specific key names and key combinations, apply bold and use the following guidelines:

Guideline | Example
--- | ---
When telling users to *type* a letter key (as in a command), use lowercase for the letter unless uppercase is required. Use *type* or *enter* when the action results in output on the interface. | When prompted, type ``y`` and then press **Enter**. <br /><br /> To change from command mode to insert mode, type `i`.
When telling users to press a letter key (as in a key combination), capitalize the letter. Use press when the action does not result in output on the interface. <br /> <br /> **Notes:** <br /><br /> Do not use the verbs *hit*, *strike*, or *punch*. <br /><br /> Separate the key names by **-** or **+**, depending on whether you are documenting Linux or Windows. If you are documenting for both, pick one symbol and use it consistently. | When you are finished, press **Ctrl+X** to exit, type `y` to confirm your changes, and then press **Enter** to save as the indicated file. <br /><br /> Press **F3** to find the next matching process, or press **Esc** to quit the search. <br /><br /> To move forward word by word, press **W**. To move back word by word, press **B**.
Avoid using *key* with specific key names. <br /><br /> If needed for clarity, on the first use of a key name, you can use the definite article *the* and *key* with the name. On subsequent uses, refer to the key only by its name. | Press **F3** to find the next matching process, or press **Esc** to quit the search. <br /><br /> Press the Help key (**F1**).
To show a key combination, use a plus sign between the names of the keys.	| To toggle between the progress bar screen and a Linux TTY screen, press **Ctrl+Alt+F2**.
If part of a key combination requires the use of the **Shift** key (such as typing an asterisk or an uppercase letter), add **Shift** to the combination and then provide the name or symbol that results from pressing **Shift** (such as ***** or **P**). | To jump to the end of the file, press **Shift+G**. <br /><br /> To apply the general number format, press **Ctrl+Shift+~**.

## <a name="links"></a>Links and cross-references
Use cross-references to help customers navigate content and find content that is related to what they are currently viewing. Cross-references can be linked or not linked, depending on the location of the content to which you are referring.

- When you refer to content within the same article or section—such as paragraphs, tables, figures, examples, and lists—you usually create a simple textual cross-reference that is not linked.

  **Note:** Customers usually expect links to take them to a location outside of the article (How-To) or section (API) that they are currently reading, so links that just jump to another place in the same article or section can be confusing. Exceptions are a TOC, or *jump list*, at the top of an article or section that provides links to the high-level headings in the article or section, and "back to top" links that take the user back to the top of the page.

- When you refer to other content that is created by Rackspace—for example, another article, a different section in the same or a different API guide, a post on the Communities site, or a pricing page on rackspace.com—you provide a link to that content.

- When you refer to content that is created outside of Rackspace, you usually provide a link to that content. Ensure that the link is active and that the content is up-to-date. Periodically check the link and content.

This topic provides the following guidelines for creating clear and specific cross-references and links:

- [General cross-reference guidelines](#general-xref)
- [Linking guidelines](#link-guidelines)
  - [Placement of links](#link-placement)
  - [Construction and format of links](#link-construction)

**Note:** In the examples in this section, links are indicated by underlines.  

### <a name="general-xref"></a>General cross-reference guidelines
When you create a cross-reference sentence to point to other information, linked or not, observe the following guidelines:

- Begin a cross-reference sentence by explaining the purpose or benefit of the cross-reference (such as more information or examples). Providing this context helps customers decide whether to follow the reference.

- Use *information about* rather than *information on*.

- Do not use *above*, *below*, *earlier*, or *later* to locate information. Use *preceding* and *following* to refer to the following items:
  - Figures, tables, and examples
  - Paragraphs or other textual information
  - Lists

Use | Avoid
--- | ---
For more information about the protocols that you can choose when configuring a load balancer, see <u>Choosing the right protocol</u>. |	See <u>Choosing the right protocol</u> for more information about the protocols that you can choose when configuring a load balancer.
Snapshots are described in <u>Create and use Cloud Block Storage snapshots</u>. |	Snapshots are described <u>later in this Getting Started Guide</u>.
The following table lists the OpenStack versions and components supported by the current releases of Rackspace Private Cloud.	| The table below lists the OpenStack versions and components supported by the current releases of Rackspace Private Cloud.

### <a name="link-guidelines"></a>Linking guidelines
When you provide links, observe the following guidelines for placement, construction, and formatting.

#### <a name="link-placement"></a>Placement of links
- Determine whether the link should be provided inline or at the end of the article or section.
  - Provide links inline only when it is necessary or helpful for the customer to follow the link to understand the current topic or complete the task. Remember that links disrupt the narrative flow and can be distracting.
  - Provide links to related but not essential information at the end of the article or section.
  - Provide links to "next steps" at the end of an article or section.


- Do not link to information more than once in an article or section.

#### <a name="link-construction"></a>Construction and format of links
- Ensure that the text of a link sufficiently describes the content to which it links (the destination content). When you provide a link at the end of an article or section to related information or to a next step, use the title of or a heading in the destination content as the link text.
  - When links are inline, use about three or four words of existing text as the link text. Choose words that best describe the destination content.
  - If existing text cannot sufficiently describe the destination content, create a cross-reference sentence for the link. For the link text, use the title of or a heading in the destination content, if possible. Avoid providing an actual URL, unless you think that having the URL is helpful for the customer.
  - Do not provide links from ambiguous phrases such as *Click here* or *More information*.


- If a link points to a location other than the current site (for example, out of the Support website or away from developer.rackspace.com), provide context that describes the location.

- When you refer to a Rackspace product or service, provide a link to the page for that product or service on www.rackspace.com. Create the link by inserting the term product page in brackets after the product name, and using that text as the link. For example, "Cloud Load Balancers [<u>product page</u>] . . ."  

- Do not code a link to open in a new tab or window. Customers can choose whether they want open a link in a new tab or window.

- If your article or section has multiple subheadings, provide a TOC (jump list) at the beginning of the article or section, after an introduction. Use the heading text as the link text, and typically link only to the top-level headings in the article or section.

  **Note:** If the UI automatically builds a TOC or jump list for the article, do not duplicate it by creating one manually within the article.

- In FAQ articles, insert a "back to top" link after each answer. Use the following HTML, which superscripts the link to make it less obtrusive: ``<p><sup><a href="#top">back to top</a></sup></p>``

  **Note:** Do not create back-to-top links in How-To FAQ articles that have automatic formatting that collapses the Q&A pairs. For these articles, such links are meaningless.

- Do not use quotation marks around link text.

- Create and format links according to the authoring tool that you are using. Test links to ensure that they are live and that they point to the correct destination.

Use | Avoid
--- | ---
The most current versions of all SDKs are located in the <u>SDK guide</u>. | The most current versions of all SDKs are located in the SDK guide: http://docs.rackspace.com/sdks/guide/content/intro.html.
You can obtain the key by logging in to the <u>Cloud Control Panel</u> and selecting **Account Settings** from the ***yourAccount*** menu in the top-right corner of the window. | You can obtain the key from the Cloud Control Panel by selecting **Account Settings** from the ***yourAccount*** menu in the top-right corner of the window. (Log in at https://mycloud.rackspace.com/.)
If you want your additional storage to be more portable or you need to be able to take data snapshots, consider <u>adding one or more volumes</u> to the new server. |	If you want your additional storage to be more portable or you need to be able to take data snapshots, consider adding one or volumes to the new server. See <u>Create and Attach a Cloud Block Storage Volume</u>.
Set the transmit rate for **Warning** and **Critical State**. (For more information about transmit rates, see <u>Rackspace Cloud Monitoring checks and alarms</u>.) |	Set the transmit rate for **Warning** and **Critical State**. (For more information about what this means, click <u>here</u>.)
If you need assistance opening the web console, see <u>Managing your server 2 - console session</u>.	| If you need assistance opening the web console, see <u>this article</u>.
Download PuTTY from <u>the PuTTY website</u>. |	<u>Download PuTTY</u>.  
For more information about cross-domain XML files, read the <u>Cross-domain policy file specification</u> article on the Adobe website. |	For more information about cross-domain XML files, go to <u>Adobe's website</u>.
Cloud Load Balancers [<u>product page</u>] has a content caching feature that stores recently accessed files on the load balancer for easy retrieval by web clients. *(when linking to the www.rackspace.com product page)* |	<u>Cloud Load Balancers</u> has a content caching feature that stores recently accessed files on the load balancer for easy retrieval by web clients. *(when linking to the www.rackspace.com product page)*

## <a name="lists-1"></a>Lists
A list is a series of parallel items that are presented together, usually in a vertical sequence. The following types of lists are commonly used in Rackspace documentation:

- **Ordered lists**, which are numbered. The list items must be performed or considered in a particular order.
- **Unordered lists** (also referred to as itemized or bullet lists), which are usually delineated by bullets. The list items can be presented in any order and are often alphabetized if no other order is more appropriate.
When three or more serial items are embedded in a paragraph, consider recasting the text as an introduction followed by an unordered list.
- **Definition lists**, which are used to define variables, parameters, attributes, terms, and so on in API documents.

This topic provides the following guidelines for lists:

- [Writing introductory text for lists](#lists-intro)
- [Writing list items](#lists-writing)

### <a name="lists-intro"></a>Writing introductory text for lists
All lists are preceded by introductory text that provides the context for the list. One exception is procedures, which can be preceded only by a procedure title. Use the following guidelines when introducing lists.

Guideline | Example
--- | ---
Introduce a list with a sentence, and end the sentence with a colon. If another sentence intervenes between the introductory sentence and the first list item, end the introductory sentence with a period instead of a colon. <br /> <br /> In a procedure, apply this guideline to text that introduces a list of substeps. <br /> <br /> **Note:** Avoid using fragments to introduce lists. Fragments are difficult to translate and can be harder to comprehend than sentences. | You can use this product to perform the following tasks: <br /> <br /> You can use this product to perform the following tasks. You must extract objects from the database to complete these tasks.
For a partial list, use the verb include in the introductory text. | The directory includes the following files: <br /> <br /> (*Includes* is correct only if you are listing some, but not all, files in the directory.)
Do not quantify items in introductory text. Quantifying items could cause an error if the list changes. | *Use:* <br /> The following methods are available: <br /> <br /> *Do not use:* <br /> The following three methods are available:
Don’t tell users to "do the following." The verb *do* is weak, using *following* as a noun in this context is incorrect, and the whole phrase is ambiguous. <br /> <br /> Use a stronger and more meaningful verb. Use *following* only as an adjective, unless you are referring to an entourage, posse, retinue, or group of fans. Ensure that the introduction to a list provides enough context for users to understand what information the list is providing. | *Use:* <br /> You can use this product to perform the following tasks: <br /><br /> The following methods are available: <br /> <br /> *Do not use:* <br /> You can use this product to do the following: <br /><br /> The following are available:

### <a name="lists-writing"></a>Writing list items
Use the following guidelines when writing list items:

- Capitalize the first letter of each list item unless the first letter must be lowercase.
- Make all list items parallel. For example, all items start with fragments, or all items use sentences. A list can have a mix of fragments and sentences as long as all of the items start with a fragment.
- Use the following guidelines for punctuation of list items:
  - In a list of only sentences, including imperative statements, use punctuation at the end of each item.
  - In a list of only fragments, use no punctuation at the end of each item.
  - In a list of fragments, some or all of which are followed by sentences, use punctuation at the end of every fragment and sentence in the list.
- Do not connect separate list items with commas or conjunctions (*and*, *or*).
- Avoid using articles (*a*, *an*, *the*) to start list items.
- When a list provides a series of terms or phrases and then more information about them, format the list as follows:
  - Show the term or phrase in bold. Using bold makes the list easier to scan.
  - If you need to separate the initial term or phrase from the information that follows it, use an em dash with no spaces on either side of it. However, if you do not need a separator, don't use one. (For an example of a list in which em dash separators are not necessary, see the list at the top of this topic.)
- Unless another order makes sense or is preferable, alphabetize list items.

The following sections show examples of the indicated types of lists.

#### All list items are sentences&mdash;example
When you create an isolated network, the following limitations apply:
- The isolated network must exist in the same region as the server.
- You can create up to three isolated networks with up to 64 servers attached to each one.
- After you create an isolated network, you cannot rename it.

#### All list items are fragments&mdash;example
The example creates a database instance called myrackinstance with the following characteristics:
- 512 MB instance flavor
- Volume size of 2 GB
- Database named `sampledb` with a `utf8` character set and a `utf8_general_ci` collation
- User named `simplestUser` with the password `password`

#### All list items are imperative statements&mdash;example
You can use Cloud Backup to perform the following actions:
- Select the files and folders from your server that you want to back up.
- Run your backups manually or on a schedule.
- See the activity from all your backups.
- Use AES-256 encryption with a private encryption key that only you know.
- Restore individual files and folders from a particular date.
- Save space with incremental backups that save only the changed portions of files.
- Create unlimited backups.

#### List items mix fragments and sentences&mdash;example
To run the examples in this guide, the following prerequisites are required:
- Rackspace Cloud account. To sign up for a Rackspace Cloud account, go to the <u>Rackspace Public Cloud signup page</u>.
- Rackspace user name and password that you specified during registration.

#### List that provides terms and more information&mdash;example
You have the following choices for your virtual IP:
- **Public**&mdash;This setting allows any two servers with public IP addresses to be load balanced. These can be nodes outside of the Rackspace network, but if they are, standard bandwidth rates apply.
- **Shared Virtual IP**&mdash;Use this setting if you want to load-balance multiple services on different ports while using the same virtual IP address.
- **Private Rackspace network**&mdash;This is the best option for load-balancing two Cloud Servers because it allows the load-balancing traffic to run on the Rackspace Cloud internal network, called ServiceNet. This option has two distinct advantages: the rate limit is double what the rate limit is on the public interface, and all traffic on the ServiceNet between Cloud Servers is not charged for bandwidth.
