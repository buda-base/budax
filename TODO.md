# BudaX How-to Guides

[\- testing site -](http://library-dev.bdrc.io/static/budax/menu/menu)

_BudaX how-to guides give users of BUDA many tips and tricks to make the most of BUDA's data. All BudaX  how-to guides include both a pre-test and a post-test questionnaire. This allows us to track the increase in knowledge of our audience so we can improve the content in a timely manner._

How-to guides are made available to 1. any BUDA user (public url), or 2. users who are part of a training program (url assigned to a specific trainer). The questionnaires on public how-to guides are published with the source tag `1`:

*   tutorial: [`http://buda.zju.edu.cn/static/howtoguides/pdf24?src=1`](http://buda.zju.edu.cn/static/howtoguides/pdf24?source=1)
*   iframe url: `https://shimowendang.com/forms/<form-id>/fill?channel=1`

When part of a training source tags go from `2` to `9` allowing us to track the performance of individual trainers. 

*   tutorial: [`http://buda.zju.edu.cn/static/howtoguides/pdf24?src=8`](http://buda.zju.edu.cn/static/howtoguides/pdf24?source=1)
*   iframe url: `https://shimowendang.com/forms/<form-id>/fill?channel=8`

Most how-to guides contain the following elements:

*   pre-test form
    *   iframe of a shimo.im form with a source tag `fill?channel=1`
*   content
    *   text
    *   gifs
    *   video iframes
*   post-test form
    *   iframe of a shimo.im form with a source tag `fill?channel=1`



## Linking between guides

### menu --> howtoguide
Syntax: `[](../howtoguides/<guide-code>/index)`

Example (in menu): `[VSC00 - ཁོ་ཌི་མཉེན་ཆས་འཇུག་སྤྲོད་བྱ་ཚུལ། 安装VS Code](../howtoguides/VSC00/index)`

### howtoguide --> menu
Syntax: `[](../../menu/menu)`

Example (in VSC00): `[BUDA 操作指南 བུདྡྷ་དྲ་བའི་བཀོལ་སྤྱོད་ལམ་སྟོན།](../../menu/menu)`
### howtoguide <--> howtoguide : 
Syntax: `[](../<guide-code>/index)`

Example (in VSC01): `[ཁོ་ཌི་མཉེན་ཆས་སྒེའུ་ཁུང་རྟགས་ཅན་ནང་ཕབ་སྟངས།](../VSC00/index)`

## Set image width in MD

Syntax: `![<width-pix>](<image-path>)`
Example: `![300](images/img.png)`

## TODO (no videos; gifs + images)

*   All (NT)
    *   resize gifs
        *   script to
     *   update overall CSS
*   MENU (NT)
    *   look better
    *   delete courses without links
*   BDRC Mobile (Dhondrup)
   *     Sections
      *     ...
*   BUDA website (...)

*   PDF24 (Lobsang)
    *   replace video
    *   make course about BDRC resources
        *   download PDF + split + merge
        *   download several PDFs + merge
        
    *   delete banner and keywords like དཔྱད་རྩོམ། or སློབ་ཚན།
    *   headings for TOC
    *   add questionnaire
*   DFC01 (Lobsang) - ནགས་ཕྱི་འཚོལ་ཆས་བཀོལ་ཚུལ། Docfetcher 搜索软件的使用方法
    *   delete or update links
    *   Docfetcher and Java download links from China
    *   delete banner and keywords like དཔྱད་རྩོམ། or སློབ་ཚན།
    *   headings for TOC
    *   add questionnaire
*    DFC02 (Lobsang) - ནགས་ཕྱི་འཚོལ་ཆས་བཀོལ་ནས་དཔྱད་རྩོམ་ཀྱི་བརྗོད་བྱ་གཏན་འབེབས། 用Docfetcher搜索来明确论文的主题
    *   Take out things about academic research
    *   headings for TOC
    *   add questionnaire
*   VSC00 (Dhondrup) - ཁོ་ཌི་མཉེན་ཆས་འཇུག་སྤྲོད་བྱ་ཚུལ། 安装VS Code
    *   Sections:
        *   Add how to download
        *   Install
        *   change font
    *   move download link to official VS Code [https://code.visualstudio.com/download#](https://code.visualstudio.com/download#) 
    *   delete or update links
    *   delete banner and keywords like དཔྱད་རྩོམ། or སློབ་ཚན།
    *   headings for TOC
    *   add questionnaire
*   VSC01 (Dhondrup) - སྤྱིར་བཏང་ཁོ་ཌི་མཉེན་ཆས་བཀོལ་སྟངས། Code软件的一般应用方式
    *   Sections:
        *   link to VSC00
        *   open folder - TODO
        *   open file - TODO
        *   search all
        *   search in file
    *   delete these sections: download, install, change font
    *   delete or update links
    *   delete banner and keywords like དཔྱད་རྩོམ། or སློབ་ཚན།
    *   headings for TOC
    *   add questionnaire
*   VSC02 (Dhondrup) - ཁོ་ཌི་མཉེན་ཆས་ནང་ལས་གནས་བཟོ་ཚུལ། Code软件上设置工作区的课程
    *   Sections:
        *   link to VSC00, VSC01
        *   ...
    *   take out section on how to install, replace with link to VSC00
    *   delete or update links
    *   delete banner and keywords like དཔྱད་རྩོམ། or སློབ་ཚན།
    *   headings for TOC
    *   add questionnaire
*   VSC03 (Dhondrup) - ཐ་སྙད་ཞིབ་འཇུག་གི་རྒྱུ་ཆ་འཚོལ་བསྡུ་བྱ་ཚུལ། 研究词汇的含义
    *   Change title to: "4 ways to search for the meaning of a term"
    *   Sections:
        *   ངོ་སྤྲོད། ཐ་སྙད་ཞིབ་འཇུག་ཐབས་ལམ་༤ ཡོད་པའི་སྐོར། 
            *   ༡
            *   ༢
        *   VS Code
            *   ཀ
            *   ཁ
        *   Doctfecher
            *   ག
        *   BUDA
            *   ང
        *   མཁས་པ།
            *   ༣
            *   ༤
            *   ༥
            *   ༦
            *   ༧
            *   ༨
            *   ༩
    *   delete or update links
    *   delete banner and keywords like དཔྱད་རྩོམ། or སློབ་ཚན།
    *   headings for TOC
    *   add questionnaire
*   VSC04 (Lobsang) - ཀཱར་ཥཱ་པ་ཎའི་སྐོར་གྱི་གཞི་གྲངས་བསྡུ་རུབ། 收集Karshapana一词的相关数据
    *   Change title: "How to find a term spelled different ways with regexes"
    *   Sections:
        *   ...
    *   put regex in code style `like this`
    *   delete or update links
    *   delete banner and keywords like དཔྱད་རྩོམ། or སློབ་ཚན།
    *   headings for TOC
    *   add questionnaire
*   SAY01 (Dhondrup Done) - Saymoreམཉེན་ཆས་བཀོལ་ནས་དཔྱད་རྩོམ་གྱི་རྒྱུ་ཆ་བསྡུ་ཚུལ། 使用Saymore软件搜集论文资料
    *   Change title: "Use Saymore to sync a lecture with an etext"
    *   Sections:
        *   delete search engine
        *   delete ༡༽ survey questions
        *   TODO intro about make audio/video searchable by syncing with an etext
    *   delete or update links
    *   delete banner and keywords like དཔྱད་རྩོམ། or སློབ་ཚན།
    *   headings for TOC
    *   add questionnaire
*   EDG01 - take out
    
*   FNT01 (Lobsang) - ཡིག་གཟུགས་ཕན་ཚུན་བསྒྱུར་ཆས། Tibetan Font Converter 藏文的字体转换器
    *   Sections:
        *   intro: to contribute etexts to BUDA you need to convert them to Unicode
        *   ...
    *   update this type of things: "Kyi stangs go_rim la gzigs"
    *   delete or update links
    *   delete banner and keywords like དཔྱད་རྩོམ། or སློབ་ཚན།
    *   headings for TOC
    *   add questionnaire
