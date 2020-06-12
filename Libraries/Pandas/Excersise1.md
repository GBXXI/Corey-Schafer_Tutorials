<script>
  function code_toggle() {
    if (code_shown){
      $('div.input').hide('500');
      $('#toggleButton').val('Show Code')
    } else {
      $('div.input').show('500');
      $('#toggleButton').val('Hide Code')
    }
    code_shown = !code_shown
  }

  $( document ).ready(function(){
    code_shown=false;
    $('div.input').hide()
  });
</script>
<form action="javascript:code_toggle()"><input type="submit" id="toggleButton" value="Show Code"></form>

```python
import pandas as pd
```


```python
df = pd.read_csv('D:\\Test GB Python\\Corey Schafer_Tutorials\\Pandas\\developer_survey_2019\\survey_results_public.csv')
schema_df = pd.read_csv('D:\\Test GB Python\\Corey Schafer_Tutorials\\Pandas\\developer_survey_2019\\survey_results_schema.csv')
```


```python
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)
```


```python
df.head()

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Respondent</th>
      <th>MainBranch</th>
      <th>Hobbyist</th>
      <th>OpenSourcer</th>
      <th>OpenSource</th>
      <th>Employment</th>
      <th>Country</th>
      <th>Student</th>
      <th>EdLevel</th>
      <th>UndergradMajor</th>
      <th>EduOther</th>
      <th>OrgSize</th>
      <th>DevType</th>
      <th>YearsCode</th>
      <th>Age1stCode</th>
      <th>YearsCodePro</th>
      <th>CareerSat</th>
      <th>JobSat</th>
      <th>MgrIdiot</th>
      <th>MgrMoney</th>
      <th>MgrWant</th>
      <th>JobSeek</th>
      <th>LastHireDate</th>
      <th>LastInt</th>
      <th>FizzBuzz</th>
      <th>JobFactors</th>
      <th>ResumeUpdate</th>
      <th>CurrencySymbol</th>
      <th>CurrencyDesc</th>
      <th>CompTotal</th>
      <th>CompFreq</th>
      <th>ConvertedComp</th>
      <th>WorkWeekHrs</th>
      <th>WorkPlan</th>
      <th>WorkChallenge</th>
      <th>WorkRemote</th>
      <th>WorkLoc</th>
      <th>ImpSyn</th>
      <th>CodeRev</th>
      <th>CodeRevHrs</th>
      <th>UnitTests</th>
      <th>PurchaseHow</th>
      <th>PurchaseWhat</th>
      <th>LanguageWorkedWith</th>
      <th>LanguageDesireNextYear</th>
      <th>DatabaseWorkedWith</th>
      <th>DatabaseDesireNextYear</th>
      <th>PlatformWorkedWith</th>
      <th>PlatformDesireNextYear</th>
      <th>WebFrameWorkedWith</th>
      <th>WebFrameDesireNextYear</th>
      <th>MiscTechWorkedWith</th>
      <th>MiscTechDesireNextYear</th>
      <th>DevEnviron</th>
      <th>OpSys</th>
      <th>Containers</th>
      <th>BlockchainOrg</th>
      <th>BlockchainIs</th>
      <th>BetterLife</th>
      <th>ITperson</th>
      <th>OffOn</th>
      <th>SocialMedia</th>
      <th>Extraversion</th>
      <th>ScreenName</th>
      <th>SOVisit1st</th>
      <th>SOVisitFreq</th>
      <th>SOVisitTo</th>
      <th>SOFindAnswer</th>
      <th>SOTimeSaved</th>
      <th>SOHowMuchTime</th>
      <th>SOAccount</th>
      <th>SOPartFreq</th>
      <th>SOJobs</th>
      <th>EntTeams</th>
      <th>SOComm</th>
      <th>WelcomeChange</th>
      <th>SONewContent</th>
      <th>Age</th>
      <th>Gender</th>
      <th>Trans</th>
      <th>Sexuality</th>
      <th>Ethnicity</th>
      <th>Dependents</th>
      <th>SurveyLength</th>
      <th>SurveyEase</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>I am a student who is learning to code</td>
      <td>Yes</td>
      <td>Never</td>
      <td>The quality of OSS and closed source software ...</td>
      <td>Not employed, and not looking for work</td>
      <td>United Kingdom</td>
      <td>No</td>
      <td>Primary/elementary school</td>
      <td>NaN</td>
      <td>Taught yourself a new language, framework, or ...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4</td>
      <td>10</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>HTML/CSS;Java;JavaScript;Python</td>
      <td>C;C++;C#;Go;HTML/CSS;Java;JavaScript;Python;SQL</td>
      <td>SQLite</td>
      <td>MySQL</td>
      <td>MacOS;Windows</td>
      <td>Android;Arduino;Windows</td>
      <td>Django;Flask</td>
      <td>Flask;jQuery</td>
      <td>Node.js</td>
      <td>Node.js</td>
      <td>IntelliJ;Notepad++;PyCharm</td>
      <td>Windows</td>
      <td>I do not use containers</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Yes</td>
      <td>Fortunately, someone else has that title</td>
      <td>Yes</td>
      <td>Twitter</td>
      <td>Online</td>
      <td>Username</td>
      <td>2017</td>
      <td>A few times per month or weekly</td>
      <td>Find answers to specific questions;Learn how t...</td>
      <td>3-5 times per week</td>
      <td>Stack Overflow was much faster</td>
      <td>31-60 minutes</td>
      <td>No</td>
      <td>NaN</td>
      <td>No, I didn't know that Stack Overflow had a jo...</td>
      <td>No, and I don't know what those are</td>
      <td>Neutral</td>
      <td>Just as welcome now as I felt last year</td>
      <td>Tech articles written by other developers;Indu...</td>
      <td>14.0</td>
      <td>Man</td>
      <td>No</td>
      <td>Straight / Heterosexual</td>
      <td>NaN</td>
      <td>No</td>
      <td>Appropriate in length</td>
      <td>Neither easy nor difficult</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>I am a student who is learning to code</td>
      <td>No</td>
      <td>Less than once per year</td>
      <td>The quality of OSS and closed source software ...</td>
      <td>Not employed, but looking for work</td>
      <td>Bosnia and Herzegovina</td>
      <td>Yes, full-time</td>
      <td>Secondary school (e.g. American high school, G...</td>
      <td>NaN</td>
      <td>Taken an online course in programming or softw...</td>
      <td>NaN</td>
      <td>Developer, desktop or enterprise applications;...</td>
      <td>NaN</td>
      <td>17</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>I am actively looking for a job</td>
      <td>I've never had a job</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Financial performance or funding status of the...</td>
      <td>Something else changed (education, award, medi...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>C++;HTML/CSS;Python</td>
      <td>C++;HTML/CSS;JavaScript;SQL</td>
      <td>NaN</td>
      <td>MySQL</td>
      <td>Windows</td>
      <td>Windows</td>
      <td>Django</td>
      <td>Django</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Atom;PyCharm</td>
      <td>Windows</td>
      <td>I do not use containers</td>
      <td>NaN</td>
      <td>Useful across many domains and could change ma...</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Instagram</td>
      <td>Online</td>
      <td>Username</td>
      <td>2017</td>
      <td>Daily or almost daily</td>
      <td>Find answers to specific questions;Learn how t...</td>
      <td>3-5 times per week</td>
      <td>Stack Overflow was much faster</td>
      <td>11-30 minutes</td>
      <td>Yes</td>
      <td>A few times per month or weekly</td>
      <td>No, I knew that Stack Overflow had a job board...</td>
      <td>No, and I don't know what those are</td>
      <td>Yes, somewhat</td>
      <td>Just as welcome now as I felt last year</td>
      <td>Tech articles written by other developers;Indu...</td>
      <td>19.0</td>
      <td>Man</td>
      <td>No</td>
      <td>Straight / Heterosexual</td>
      <td>NaN</td>
      <td>No</td>
      <td>Appropriate in length</td>
      <td>Neither easy nor difficult</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>I am not primarily a developer, but I write co...</td>
      <td>Yes</td>
      <td>Never</td>
      <td>The quality of OSS and closed source software ...</td>
      <td>Employed full-time</td>
      <td>Thailand</td>
      <td>No</td>
      <td>Bachelor’s degree (BA, BS, B.Eng., etc.)</td>
      <td>Web development or web design</td>
      <td>Taught yourself a new language, framework, or ...</td>
      <td>100 to 499 employees</td>
      <td>Designer;Developer, back-end;Developer, front-...</td>
      <td>3</td>
      <td>22</td>
      <td>1</td>
      <td>Slightly satisfied</td>
      <td>Slightly satisfied</td>
      <td>Not at all confident</td>
      <td>Not sure</td>
      <td>Not sure</td>
      <td>I’m not actively looking, but I am open to new...</td>
      <td>1-2 years ago</td>
      <td>Interview with people in peer roles</td>
      <td>No</td>
      <td>Languages, frameworks, and other technologies ...</td>
      <td>I was preparing for a job search</td>
      <td>THB</td>
      <td>Thai baht</td>
      <td>23000.0</td>
      <td>Monthly</td>
      <td>8820.0</td>
      <td>40.0</td>
      <td>There's no schedule or spec; I work on what se...</td>
      <td>Distracting work environment;Inadequate access...</td>
      <td>Less than once per month / Never</td>
      <td>Home</td>
      <td>Average</td>
      <td>No</td>
      <td>NaN</td>
      <td>No, but I think we should</td>
      <td>Not sure</td>
      <td>I have little or no influence</td>
      <td>HTML/CSS</td>
      <td>Elixir;HTML/CSS</td>
      <td>PostgreSQL</td>
      <td>PostgreSQL</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Other(s):</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Vim;Visual Studio Code</td>
      <td>Linux-based</td>
      <td>I do not use containers</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Reddit</td>
      <td>In real life (in person)</td>
      <td>Username</td>
      <td>2011</td>
      <td>A few times per week</td>
      <td>Find answers to specific questions;Learn how t...</td>
      <td>6-10 times per week</td>
      <td>They were about the same</td>
      <td>NaN</td>
      <td>Yes</td>
      <td>Less than once per month or monthly</td>
      <td>Yes</td>
      <td>No, I've heard of them, but I am not part of a...</td>
      <td>Neutral</td>
      <td>Just as welcome now as I felt last year</td>
      <td>Tech meetups or events in your area;Courses on...</td>
      <td>28.0</td>
      <td>Man</td>
      <td>No</td>
      <td>Straight / Heterosexual</td>
      <td>NaN</td>
      <td>Yes</td>
      <td>Appropriate in length</td>
      <td>Neither easy nor difficult</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>I am a developer by profession</td>
      <td>No</td>
      <td>Never</td>
      <td>The quality of OSS and closed source software ...</td>
      <td>Employed full-time</td>
      <td>United States</td>
      <td>No</td>
      <td>Bachelor’s degree (BA, BS, B.Eng., etc.)</td>
      <td>Computer science, computer engineering, or sof...</td>
      <td>Taken an online course in programming or softw...</td>
      <td>100 to 499 employees</td>
      <td>Developer, full-stack</td>
      <td>3</td>
      <td>16</td>
      <td>Less than 1 year</td>
      <td>Very satisfied</td>
      <td>Slightly satisfied</td>
      <td>Very confident</td>
      <td>No</td>
      <td>Not sure</td>
      <td>I am not interested in new job opportunities</td>
      <td>Less than a year ago</td>
      <td>Write code by hand (e.g., on a whiteboard);Int...</td>
      <td>No</td>
      <td>Languages, frameworks, and other technologies ...</td>
      <td>I was preparing for a job search</td>
      <td>USD</td>
      <td>United States dollar</td>
      <td>61000.0</td>
      <td>Yearly</td>
      <td>61000.0</td>
      <td>80.0</td>
      <td>There's no schedule or spec; I work on what se...</td>
      <td>NaN</td>
      <td>Less than once per month / Never</td>
      <td>Home</td>
      <td>A little below average</td>
      <td>No</td>
      <td>NaN</td>
      <td>No, but I think we should</td>
      <td>Developers typically have the most influence o...</td>
      <td>I have little or no influence</td>
      <td>C;C++;C#;Python;SQL</td>
      <td>C;C#;JavaScript;SQL</td>
      <td>MySQL;SQLite</td>
      <td>MySQL;SQLite</td>
      <td>Linux;Windows</td>
      <td>Linux;Windows</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>.NET</td>
      <td>.NET</td>
      <td>Eclipse;Vim;Visual Studio;Visual Studio Code</td>
      <td>Windows</td>
      <td>I do not use containers</td>
      <td>Not at all</td>
      <td>Useful for decentralized currency (i.e., Bitcoin)</td>
      <td>Yes</td>
      <td>SIGH</td>
      <td>Yes</td>
      <td>Reddit</td>
      <td>In real life (in person)</td>
      <td>Username</td>
      <td>2014</td>
      <td>Daily or almost daily</td>
      <td>Find answers to specific questions;Pass the ti...</td>
      <td>1-2 times per week</td>
      <td>Stack Overflow was much faster</td>
      <td>31-60 minutes</td>
      <td>Yes</td>
      <td>Less than once per month or monthly</td>
      <td>Yes</td>
      <td>No, and I don't know what those are</td>
      <td>No, not really</td>
      <td>Just as welcome now as I felt last year</td>
      <td>Tech articles written by other developers;Indu...</td>
      <td>22.0</td>
      <td>Man</td>
      <td>No</td>
      <td>Straight / Heterosexual</td>
      <td>White or of European descent</td>
      <td>No</td>
      <td>Appropriate in length</td>
      <td>Easy</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>I am a developer by profession</td>
      <td>Yes</td>
      <td>Once a month or more often</td>
      <td>OSS is, on average, of HIGHER quality than pro...</td>
      <td>Employed full-time</td>
      <td>Ukraine</td>
      <td>No</td>
      <td>Bachelor’s degree (BA, BS, B.Eng., etc.)</td>
      <td>Computer science, computer engineering, or sof...</td>
      <td>Taken an online course in programming or softw...</td>
      <td>10,000 or more employees</td>
      <td>Academic researcher;Developer, desktop or ente...</td>
      <td>16</td>
      <td>14</td>
      <td>9</td>
      <td>Very dissatisfied</td>
      <td>Slightly dissatisfied</td>
      <td>Somewhat confident</td>
      <td>Yes</td>
      <td>No</td>
      <td>I am not interested in new job opportunities</td>
      <td>Less than a year ago</td>
      <td>Write any code;Write code by hand (e.g., on a ...</td>
      <td>No</td>
      <td>Industry that I'd be working in;Languages, fra...</td>
      <td>I was preparing for a job search</td>
      <td>UAH</td>
      <td>Ukrainian hryvnia</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>55.0</td>
      <td>There is a schedule and/or spec (made by me or...</td>
      <td>Being tasked with non-development work;Inadequ...</td>
      <td>A few days each month</td>
      <td>Office</td>
      <td>A little above average</td>
      <td>Yes, because I see value in code review</td>
      <td>NaN</td>
      <td>Yes, it's part of our process</td>
      <td>Not sure</td>
      <td>I have little or no influence</td>
      <td>C++;HTML/CSS;Java;JavaScript;Python;SQL;VBA</td>
      <td>HTML/CSS;Java;JavaScript;SQL;WebAssembly</td>
      <td>Couchbase;MongoDB;MySQL;Oracle;PostgreSQL;SQLite</td>
      <td>Couchbase;Firebase;MongoDB;MySQL;Oracle;Postgr...</td>
      <td>Android;Linux;MacOS;Slack;Windows</td>
      <td>Android;Docker;Kubernetes;Linux;Slack</td>
      <td>Django;Express;Flask;jQuery;React.js;Spring</td>
      <td>Flask;jQuery;React.js;Spring</td>
      <td>Cordova;Node.js</td>
      <td>Apache Spark;Hadoop;Node.js;React Native</td>
      <td>IntelliJ;Notepad++;Vim</td>
      <td>Linux-based</td>
      <td>Outside of work, for personal projects</td>
      <td>Not at all</td>
      <td>NaN</td>
      <td>Yes</td>
      <td>Also Yes</td>
      <td>Yes</td>
      <td>Facebook</td>
      <td>In real life (in person)</td>
      <td>Username</td>
      <td>I don't remember</td>
      <td>Multiple times per day</td>
      <td>Find answers to specific questions</td>
      <td>More than 10 times per week</td>
      <td>Stack Overflow was much faster</td>
      <td>NaN</td>
      <td>Yes</td>
      <td>A few times per month or weekly</td>
      <td>No, I knew that Stack Overflow had a job board...</td>
      <td>No, I've heard of them, but I am not part of a...</td>
      <td>Yes, definitely</td>
      <td>Just as welcome now as I felt last year</td>
      <td>Tech meetups or events in your area;Courses on...</td>
      <td>30.0</td>
      <td>Man</td>
      <td>No</td>
      <td>Straight / Heterosexual</td>
      <td>White or of European descent;Multiracial</td>
      <td>No</td>
      <td>Appropriate in length</td>
      <td>Easy</td>
    </tr>
  </tbody>
</table>
</div>



Creating a groupby object, with 'Country' as a parameter.


```python
grp_country = df.groupby('Country')

```

Applying a string method in our grouped object to see the total<br>
users of Python in each country.


```python
total_pthn = grp_country['LanguageWorkedWith'].apply(lambda pthn: pthn.str.contains('Python').sum())
total_pthn

```




    Country
    Afghanistan                              8
    Albania                                 23
    Algeria                                 40
    Andorra                                  0
    Angola                                   2
                                            ..
    Venezuela, Bolivarian Republic of...    28
    Viet Nam                                78
    Yemen                                    3
    Zambia                                   4
    Zimbabwe                                14
    Name: LanguageWorkedWith, Length: 179, dtype: int64



Counting the total interviewees by country.


```python
total_int = df['Country'].value_counts().sort_index()
total_int

```




    Afghanistan                              44
    Albania                                  86
    Algeria                                 134
    Andorra                                   7
    Angola                                    5
                                           ... 
    Venezuela, Bolivarian Republic of...     88
    Viet Nam                                231
    Yemen                                    19
    Zambia                                   12
    Zimbabwe                                 39
    Name: Country, Length: 179, dtype: int64



Creating a dataframe where we concatenate the above series.<br>
We set the parameter 'axis' equal to 'Coulumns' because by default it's going<br>
to concatenate on row


```python
pthn_df = pd.concat([total_int, total_pthn], axis='columns')
pthn_df

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>LanguageWorkedWith</th>
    </tr>
    <tr>
      <th>Country</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Afghanistan</th>
      <td>44</td>
      <td>8</td>
    </tr>
    <tr>
      <th>Albania</th>
      <td>86</td>
      <td>23</td>
    </tr>
    <tr>
      <th>Algeria</th>
      <td>134</td>
      <td>40</td>
    </tr>
    <tr>
      <th>Andorra</th>
      <td>7</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Angola</th>
      <td>5</td>
      <td>2</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>Venezuela, Bolivarian Republic of...</th>
      <td>88</td>
      <td>28</td>
    </tr>
    <tr>
      <th>Viet Nam</th>
      <td>231</td>
      <td>78</td>
    </tr>
    <tr>
      <th>Yemen</th>
      <td>19</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Zambia</th>
      <td>12</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Zimbabwe</th>
      <td>39</td>
      <td>14</td>
    </tr>
  </tbody>
</table>
<p>179 rows × 2 columns</p>
</div>



Renaming our columns for better presentation.


```python
pthn_df.rename(columns={'Country':'# Of interviewees', 'LanguageWorkedWith':'# Of Python Users'}, inplace=True)
pthn_df

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th># Of interviewees</th>
      <th># Of Python Users</th>
    </tr>
    <tr>
      <th>Country</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Afghanistan</th>
      <td>44</td>
      <td>8</td>
    </tr>
    <tr>
      <th>Albania</th>
      <td>86</td>
      <td>23</td>
    </tr>
    <tr>
      <th>Algeria</th>
      <td>134</td>
      <td>40</td>
    </tr>
    <tr>
      <th>Andorra</th>
      <td>7</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Angola</th>
      <td>5</td>
      <td>2</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>Venezuela, Bolivarian Republic of...</th>
      <td>88</td>
      <td>28</td>
    </tr>
    <tr>
      <th>Viet Nam</th>
      <td>231</td>
      <td>78</td>
    </tr>
    <tr>
      <th>Yemen</th>
      <td>19</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Zambia</th>
      <td>12</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Zimbabwe</th>
      <td>39</td>
      <td>14</td>
    </tr>
  </tbody>
</table>
<p>179 rows × 2 columns</p>
</div>



Assigning a new column for our result.


```python
pthn_df['% Python Users'] = (
(pthn_df['# Of Python Users']/pthn_df['# Of interviewees']) *100
)
pthn_df

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th># Of interviewees</th>
      <th># Of Python Users</th>
      <th>% Python Users</th>
    </tr>
    <tr>
      <th>Country</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Afghanistan</th>
      <td>44</td>
      <td>8</td>
      <td>18.181818</td>
    </tr>
    <tr>
      <th>Albania</th>
      <td>86</td>
      <td>23</td>
      <td>26.744186</td>
    </tr>
    <tr>
      <th>Algeria</th>
      <td>134</td>
      <td>40</td>
      <td>29.850746</td>
    </tr>
    <tr>
      <th>Andorra</th>
      <td>7</td>
      <td>0</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>Angola</th>
      <td>5</td>
      <td>2</td>
      <td>40.000000</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>Venezuela, Bolivarian Republic of...</th>
      <td>88</td>
      <td>28</td>
      <td>31.818182</td>
    </tr>
    <tr>
      <th>Viet Nam</th>
      <td>231</td>
      <td>78</td>
      <td>33.766234</td>
    </tr>
    <tr>
      <th>Yemen</th>
      <td>19</td>
      <td>3</td>
      <td>15.789474</td>
    </tr>
    <tr>
      <th>Zambia</th>
      <td>12</td>
      <td>4</td>
      <td>33.333333</td>
    </tr>
    <tr>
      <th>Zimbabwe</th>
      <td>39</td>
      <td>14</td>
      <td>35.897436</td>
    </tr>
  </tbody>
</table>
<p>179 rows × 3 columns</p>
</div>



Sorting based on the largest percentage, in desceding order


```python
pthn_df.sort_values(by=['% Python Users', 'Country'], ascending=[False, True], inplace=True)
pthn_df

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th># Of interviewees</th>
      <th># Of Python Users</th>
      <th>% Python Users</th>
    </tr>
    <tr>
      <th>Country</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Dominica</th>
      <td>1</td>
      <td>1</td>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>Niger</th>
      <td>1</td>
      <td>1</td>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>Sao Tome and Principe</th>
      <td>1</td>
      <td>1</td>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>Timor-Leste</th>
      <td>1</td>
      <td>1</td>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>Turkmenistan</th>
      <td>7</td>
      <td>6</td>
      <td>85.714286</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>Papua New Guinea</th>
      <td>1</td>
      <td>0</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>Saint Kitts and Nevis</th>
      <td>1</td>
      <td>0</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>Saint Vincent and the Grenadines</th>
      <td>1</td>
      <td>0</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>Tajikistan</th>
      <td>7</td>
      <td>0</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>Tonga</th>
      <td>1</td>
      <td>0</td>
      <td>0.000000</td>
    </tr>
  </tbody>
</table>
<p>179 rows × 3 columns</p>
</div>



Searching for a specific country


```python
pthn_df.loc['Greece']
```




    # Of interviewees    556.000000
    # Of Python Users    226.000000
    % Python Users        40.647482
    Name: Greece, dtype: float64


