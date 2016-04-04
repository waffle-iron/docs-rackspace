# Screenshot and diagram guidelines

At Rackspace, we strive to deliver ***Fanatical Support***® through exceptional documentation. Visuals are an essential part of helpful, clear, and concise content.
Follow the standards in this section when adding visuals to your documents.

**Note:** These guidelines conform to all of the rules outlined in the writing style guide.

- [Screenshot guidelines](#screenshot-guidelines)
- [Diagram guidelines](#diagram-guidelines)

## Screenshot guidelines

Read this topic to learn when to use and how to create and add screenshots.

- [When to use screenshots](#when-to-use-screenshots)
- [Guidelines for creating screenshots](#guidelines-for-creating-screenshots)
- [Screenshot checklist](#shotlist-checklist)
- [Choosing the color for screenshots and callouts](#choosing-the-color-for-screenshots-and-callouts)
- [Adding screenshots to a document](#adding-screenshots-to-a-document)

### When to use screenshots

When your content references a user interface (UI), consider whether you need to include screenshots. Screenshots can be helpful when text alone cannot adequately convey instructions, and users like screenshots and find them useful. However, screenshots are difficult and time-consuming to maintain and present translation problems. So you should carefully consider whether a screenshot is necessary.

Generally, you can use screenshots for the following purposes:

- Orient users in a complicated or long procedure

- Validate that what users see on the screen is correct, especially if the particular screen might be misinterpreted

- Show complex windows or dialog boxes, such as those that contain multiple subsets of information, with free-form text fields and many options available for selection.

Generally, do not include screenshot of the following items:

- Code samples (instead, show code samples in code blocks)

- Dialog boxes that are easy to understand, such as drop-down lists and option buttons with few or no free-form text fields

- Confirmation boxes

- License agreement boxes

- Message text (instead show message text within regular text)

- Progress bars

- Welcome windows

- Wizard pages, especially Welcome pages and other simple pages

- Tables created in another authoring tool

As an alternative to screenshots, use the correct names of the UI labels with which the user must interact and the values that they must choose or enter. Show the names of buttons, options, check boxes, menus, windows, dialog boxes, and so on as they appear on the UI. You might need to occasionally double-check these names to keep them up to date, but that takes less time than reproducing a whole set of outdated screenshots. For example, for straightforward instructions like, "To open a file, select **File > Open**," a screenshot is not required.

#### Scope of a screenshot

If you need to use a screenshot, limit its scope. For example, if you describing how to perform a certain action on a server through the Cloud Control Panel, include just the portion of the control panel that shows this action, plus enough surrounding detail to help the user locate the item. When you limit the scope of the screenshot, you are increasing the likelihood that it will remain valid over time.

#### Screenshots in procedures

If you include a screenshot in a procedure, place it directly under the step that it illustrates. However, do not rely on the screenshot to show information or values that the user must enter; always provide that information in the text of the steps. However, ensure that the screenshot accurately reflects the directions and values in the step text.

### Guidelines for creating screenshots

Use the following guidelines when you create screenshots:

- Software
- Size
- Callouts
- Titles (captions)
- Borders
- Name, format, and storage

#### Software

Use Jing or Skitch to capture screenshots.

- Jing is available for Mac OS X and Windows at http://www.techsmith.com/download/jing/.

- Skitch is available for Windows at https://evernote.com/skitch/?utm_source=interspire and for Mac OS X in the Mac App store.

Jing and Skitch do not support Linux distributions, but you can use other programs such as gscreendump, greenshot, and shutter on Linux.

When you generate screenshots from a program other than Jing or Skitch, follow the screenshot standards.

#### Size
Use the following guiding principle for screenshots: Capture only the elements that you are describing, but give enough surrounding detail to help the customer figure out where the element is.

You do not have to capture the entire screen or the entire web browser.

Screenshots should not be larger than 600 pixels wide.

#### Callouts
If you need to add callouts to direct the reader's attention, use only arrows and boxes.

For callouts and arrows, use the color 00CC33 in hexidecimal. To get this color in Jing and Skitch, see [Choosing the color for screenshots and callouts](#choosing-the-color-for-screenshots-and-callouts).

#### Titles
As a general rule, screenshots should have titles (also called *captions*). However, screenshots in procedures and tutorials do not normally require titles.

When creating titles for screenshots, use the following guidelines:

- Use sentence-style capitalization. For detailed guidelines, see [Capitalization of titles and headings](a-l-style-guidelines.md#cap-titles).

- Do not start a title with an article (*a*, *an*, or *the*).

- Do not end a title with a period.

- Make titles meaningful, descriptive, and concise:
  - Avoid using a title that duplicates an article or section title.

  - Ensure that no two titles are identical. To distinguish between the titles that are similar, add a qualifier.


- Do not include trademark symbols in titles.

- Place the title above the screenshot, not below it.

#### Borders

<!--- Find out if we have the same border requirements.
-->

Borders should be 2px black around images. You can create borders by using a screenshot editing tool such as Jing or Skitch or by using a CSS.

If you are using a CSS, add the following style information within the `<img>` tag to create the border:

    <img style="border: 2px solid black;" src="screenshotFileName.png"></img>

#### Name, format, and storage

Give your screenshot files unique and meaningful names. Providing meaningful file names enables easy differentiation among screenshots, which saves time and reduces errors on subsequent edits to a document.

For example, you might name a screenshot **control_panel_add_server.png**.

Ensure that screenshots are in PNG format.

<!--- Add guidelines about storage.
-->

### Screenshot checklist
Use the following checklist to ensure that screenshots meet standards:

Item | Complete?
--- | ---
Is the screenshot necessary? Does it add any value or clarity? See [When to use screenshots](#when-to-use-screenshots). |
The screenshot matches the current user interface (UI). |
The screenshot is large enough so that the customer can see it without scrolling or zooming in. |
The screenshot has a 2px black border. See [Borders](#borders). |
Any callouts follow the guidelines for callouts. See [Callouts](#callouts). |
The title follows the guidelines for titles. See [Titles](#titles). |
The screenshot file is named correctly. See [Name, format, and storage](#name-format-and-storage). | 	 

### Choosing the color for screenshots and callouts
Both Jing and Skitch (see [Software](#software)) have built-in functionality for creating frame callouts and arrows. Use this built-in functionality to promote consistency.The benefit of Skitch is that you can change the size (thickness) of your frames and arrows.

We have selected a moderate green (00CC33) for a highlight color for callouts. This is a web-safe color, which means that is appears the same way across browsers. The RGB values for this color are 0, 204, 51.  

#### To select color in Jing

1. In the menu box, click the color box.

    The application-based color selector is displayed.

    <img src="{% asset_path jing-color-selector.png %}" />

2. Click the box marked **other**.

    The OS-based color selector is displayed.

3. Click the **View Color Palettes** button.

4. Click the **Web Safe Colors** palette.

5. Select **00CC33** from the colors. Alternatively, you can enter **00CC33** in the **Search** box.

    **Note:** To enhance clarity, green was not used for the callouts in the following image.

    <img src="{% asset_path os-color-selector-jing.png%}" />

6. Double-click the color to add it to your custom color bar at the bottom.

7. Close the OS-based color selector by clicking the left-most button (the red X) in the title bar.
    The color is added for use to Jing.

#### To select color in Skitch

1. Click the dot labeled **Color**.

    The in-application color selector is displayed.

    <img src="{% asset_path skitch-with-color-option.png%}" />

2. Click the colored oval labeled **Custom**.

3. The OS-based color selector is displayed (same as with Jing).

4. Click the **View Color Palettes** button.

5. Click the **Web Safe Colors** palette.

6. Select **00CC33** from the colors. Alternatively, you can enter **00CC33** in the **Search** box.

    **Note:** To enhance clarity, green was not used for the callouts in the following image.

    <img src="{% asset_path os-color-selector-skitch.png%}" />

7. Double-click the color to add it to your custom color bar at the bottom.

8. Close the OS-based color selector by clicking the left-most button (the red X) in the title bar.

    The color is added for use to Skitch.

### Adding screenshots to a document
<!--- Add instructions.
-->
