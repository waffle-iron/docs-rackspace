# Screenshot and diagram guidelines

At Rackspace, we strive to deliver ***Fanatical Support***® through exceptional documentation. Images are an essential part of helpful, clear, and concise content. Follow the standards in this section when creating images for your documents.

**Note:** These guidelines conform to all of the rules outlined in the writing style guide.

- [Screenshot guidelines](#screenshot-guidelines)
- [Diagram guidelines](#diagram-guidelines)

**Note:** For instructions about how to add images to your files, see the **CONTRIBUTING.md** file in the content repository in GitHub.

## Screenshot guidelines

Read this topic to learn when to use and how to create and add screenshots.

- [When to use screenshots](#when-to-use-screenshots)
- [Guidelines for creating screenshots](#guidelines-for-creating-screenshots)
- [Screenshot checklist](#shotlist-checklist)
- [Choosing the color for screenshots and callouts](#choosing-the-color-for-screenshots-and-callouts)

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

- [Software](#software)
- [Size](#size)
- [Callouts](#callouts)
- [Titles](#titles)
- [Borders](#borders)
- [Name and format](#name-and-format)

#### Software

Use Jing or Skitch to capture screenshots.

- Jing is available for Mac OS X and Windows at http://www.techsmith.com/download/jing/.

- Skitch is available for Windows at https://evernote.com/skitch/?utm_source=interspire and for Mac OS X in the Mac App store.

Jing and Skitch do not support Linux distributions, but you can use other programs such as gscreendump, greenshot, and shutter on Linux.

When you generate screenshots from a program other than Jing or Skitch, follow the screenshot standards.

#### Size
Capture only the elements that you are describing, but give enough surrounding detail to help the customer figure out where the element is. You do not have to capture the entire screen or the entire web browser.

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

#### Name and format

Give your screenshot files unique and meaningful names. Providing meaningful file names enables easy differentiation among screenshots, which saves time and reduces errors on subsequent edits to a document.

For example, you might name a screenshot **control-panel-add-server.png**.

Ensure that screenshots are in PNG format.

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
The screenshot file is named correctly. See [Name and format](#name-and-format). | 	 

### Choosing the color for screenshots and callouts
Both Jing and Skitch (see [Software](#software)) have built-in functionality for creating frame callouts and arrows. Use this built-in functionality to promote consistency.The benefit of Skitch is that you can change the size (thickness) of your frames and arrows.

We have selected a moderate green (00CC33) for a highlight color for callouts. This is a web-safe color, which means that is appears the same way across browsers. The RGB values for this color are 0, 204, 51.  

#### To select color in Jing

1. In the menu box, click the color box.

    The application-based color selector is displayed.

    ![Jing color selector](https://github.com/rackerlabs/docs-rackspace/blob/master/_assets/img/jing-color-selector.png)

2. Click the box marked **other**.

    The OS-based color selector is displayed.

3. Click the **View Color Palettes** button.

4. Click the **Web Safe Colors** palette.

5. Select **00CC33** from the colors. Alternatively, you can enter **00CC33** in the **Search** box.

    **Note:** To enhance clarity, green was not used for the callouts in the following image.

    ![Jing OS color selector](https://github.com/rackerlabs/docs-rackspace/blob/master/_assets/img/os-color-selector-jing.png)

6. Double-click the color to add it to your custom color bar at the bottom.

7. Close the OS-based color selector by clicking the left-most button (the red X) in the title bar.
    The color is added for use to Jing.

#### To select color in Skitch

1. Click the dot labeled **Color**.

    The in-application color selector is displayed.

    ![Skitch color option](https://github.com/rackerlabs/docs-rackspace/blob/master/_assets/img/skitch-with-color-option.png)

2. Click the colored oval labeled **Custom**.

3. The OS-based color selector is displayed (same as with Jing).

4. Click the **View Color Palettes** button.

5. Click the **Web Safe Colors** palette.

6. Select **00CC33** from the colors. Alternatively, you can enter **00CC33** in the **Search** box.

    **Note:** To enhance clarity, green was not used for the callouts in the following image.

    ![Skitch OS color selector](https://github.com/rackerlabs/docs-rackspace/blob/master/_assets/img/os-color-selector-skitch.png)

7. Double-click the color to add it to your custom color bar at the bottom.

8. Close the OS-based color selector by clicking the left-most button (the red X) in the title bar.

    The color is added for use to Skitch.

## Diagram guidelines

A *diagram* is a schematic representation of a structure. It visually conveys how individual pieces of a structure interact with each other, usually through the use of icons, arrows, or other visuals.

If you want to create attractive diagrams that help simplify complex structures for the reader, use these guidelines:

- [When to use diagrams](#when-to-use-diagrams)
- [Using stencils and shapes](#using-stencils-and-shapes)
- [Using lines and arrows](#using-lines-and-arrows)
- [Diagram titles](#diagram-titles)
- [Diagram formatting and properties](#diagram-formatting-and-properties)
- [How to save and edit diagram files](#how-to-save-and-edit-diagram-files)
- [Best practices for diagrams](#best-practices-for-diagrams)

**Tip:** We recommend that you use [draw.io](https://www.draw.io/) to create the diagrams. Each example in this section was created with draw.io.

### When to use diagrams
Diagrams can be useful tools to help users visualize complex processes in a simplified fashion. However, diagrams can sometimes be too simplistic, confusing the user instead of providing help. Although the decision about whether a diagram might be helpful depends on the context of each document and the discretion of each writer, following are some general suggestions for appropriate places to insert diagrams:

- When there is an interaction between Rackspace products and other entities such as the web or APIs.

- When there is evidence of a process, whether the process is automated or manual. As a general rule, a process can be defined as the exchange of data between two points. Points can be anything from a API endpoint to a user entering commands through the Cloud Control Panel.

- When clarifying configurations and settings, such as the architecture for virtual servers.

Following are a few suggestions on where *not* to place diagrams:

- When a process is simplistic, such as GUI interactions
- When there is no interaction with a Rackspace product
- When a process is too complex and needs further explanation in text

### Using stencils and shapes

When you create a new diagram, use the How-To product stencils. Doing so ensures that each product (for example, Cloud Images) has a unique symbol that carries the same meaning when used across diagrams. Product stencils for diagram creation are located in [this zip file](https://github.com/rackerlabs/docs-rackspace/blob/master/_assets/zip/ProductIcons.zip). Only products in the Rackspace Cloud Infrastructure have unique stencils. For example, the following stencil is used for Cloud Images.

**Stencil for Cloud Images**

![Cloud Images stencil](https://github.com/rackerlabs/docs-rackspace/blob/master/_assets/img/images.png)

#### When to use blue stencils versus black stencils
Not all stencils that you use in diagrams will be the same color as the product stencils.

- Blue stencils represent items that a user can directly affect by using Rackspace products (for example, cloud images or scalable servers). In draw.io, the color code for blue is 297ACC.

- Black stencils represent items that the user cannot affect by using Rackspace products (for example, the web).

  The following diagram shows an example of black versus blue stencils. Cloud Files and server instances are shown in blue, whereas the web is shown in black.

  **Example of black versus blue stencils**

  ![Black versus blue stencils](https://github.com/rackerlabs/docs-rackspace/blob/master/_assets/img/StencilColorExamples.png)

- If you use symbols for third-party product (for example, the Linux penguin), use the same color scheme as the third-party symbol. The following example shows symbols from various third parties.

  **Example of third-party logo colors**

  ![Third-party logo colors](https://github.com/rackerlabs/docs-rackspace/blob/master/_assets/img/colors-logos.png)

#### New shapes and stencils
Sometimes, an object in your diagram needs a symbol that represents a function (for example, an API endpoint) instead of a product. Following are two options:

- Draw.io contains shapes that can be used in diagrams, but these shapes must conform to the look of Rackspace designed stencils. They also must be labeled.

- Rackers have drawn other stencils that you can use for diagrams. Most of these stencils appear in black, but you can change them into the same blue color as the product stencils in open-source programs such as Inkscape. These are located in [this zip file](https://github.com/rackerlabs/docs-rackspace/blob/master/_assets/zip/RackspaceDiagramIcons.zip).

**Note:** A library of Rackspace icons and their meanings can be found in [this PDF file](https://github.com/rackerlabs/docs-rackspace/blob/master/_assets/zip/rackspace-icon-library[1].pdf).

#### Label all stencils and shapes on diagrams
Although Rackspace products have unique stencils, all stencils must be labeled according to their function within the diagram. The same rule applies to shapes. Labels further clarify what each stencil or shape represents. Refer to the preceding black-versus-blue diagram for an example.

### Using lines and arrows

Lines are used to connect and display the relationship between two or more object stencils. They are customizable in appearance, can have arrows at the end, and can be solid, dashed, or dotted. Although not required, we recommend that you use the following best practices for lines in diagrams:

- Use a line width above **2pt**. You can change the width in the **Format Panel** under **Style** when you select the line.

- Keep lines straight unless a line needs to change direction.

- If the relationship between two or more stencils is specific, label the line.

- Use black lines unless colors are needed to differentiate the relationship between stencils. The following digram shows an example of using different color lines. In this example, the producer has a separate relationship with two different consumers, signified by the blue and red lines.

  **Example of lines of different colors**

  ![Lines of different colors](https://github.com/rackerlabs/docs-rackspace/blob/master/_assets/img/cloudimagesharing.png)

#### Solid lines
Solid lines typically show a direct relationships between stencils. They can also show implied relationships.

In the following example, an API endpoint has a direct relationship with two different Rackspace products, including Cloud Images.

**Example of solid lines**

![Example of solid lines](https://github.com/rackerlabs/docs-rackspace/blob/master/_assets/img/solid-lines.png)

#### Dashed lines
Dashed lines typically group stencils that are in a network.

In the following example, the potential growth for new servers is in a public network with Cloud Databases and another server.

**Example of dashed lines**

![Example of dashed lines](https://github.com/rackerlabs/docs-rackspace/blob/master/_assets/img/dashed-lines.png)

#### Dotted lines
Dotted lines typically represent the traveling of information. These lines are most likely to include arrows on either end of the line.

In the following example, the producer places a firewall (information) in front of consumer B.

**Example of dotted lines**

![Example of dotted lines](https://github.com/rackerlabs/docs-rackspace/blob/master/_assets/img/dotted-lines.png)

#### One-way and two-way arrows
Use arrows to represent direct interactions between two or more stencils. If a stencil is attached to an arrow, it implies that the product represented by the stencil needs to interact with another piece of the diagram.

In the following example, the CDN management service needs to interact with the CDN to perform it's function. Similarly, the CDN needs to be managed by the CDN management service. The relationship is two-way, so the line has arrows on both ends pointed to both stencils.

Alternatively, a CDN is needed to serve content to consumers, but those consumers only receive content from the CDN. The consumers need the CDN but the CDN does not need consumers. The relationship is one-way, so the arrow points only to the consumers.

**Example of one-way and two-way arrows**

![Example of one-way and two-way arrows](https://github.com/rackerlabs/docs-rackspace/blob/master/_assets/img/arrowsscreenshot.png)

### Diagram titles
Each diagram must have a descriptive title that explicitly states the subject of the diagram. Titles are created using a text box within draw.io and are saved directly onto the diagram.

Format the title as follows:

- Use the Tahoma font.
- Bold the title.
- Make the title at least 24px in size.
- Left-align the title above the diagram.

### Diagram formatting and properties
Use the following general guidelines to ensure uniformity across all diagrams:

- Use the Tahoma font for all captions and labels.

- Set each diagram to a Landscape format. To do this, click **File > Document properties**, and then under **Paper size**, set the drop-down menu to **A4 (210 mm x 297 mm)**. Under the drop-down menu, select **Landscape**.

- Change the background color to white. To do this, click **File > Document properties**, and then click the square next to **Background** and change the color to code **FFFFFF**.

### How to save and edit diagram files
Draw.io saves two files: an XML file, which is used to edit the diagram, and an IMG file, which is used to publish the diagram. Both files are needed to ensure that a diagram can be published as well as edited.

Following are instructions for saving and editing files.

#### Save an XML (editable) file

1. Click **File > Save As**.

2. Type a name for the file, being sure the leave **.xml** in the file name. The name should be in the format **filename.xml**.

  The file is saved in your local downloads directory. Move the file to the directory or the GitHub repository in which you want to keep the file.

#### Save an IMG (publishable) file

1. Click **File > Export As > PNG**. All IMG files should be saved as PNG).

2. Type a name for the file, being sure to leave **.png** in the file name. The name should be in the format **filename.png**.

  The file is saved in your local downloads directory. Move the file to the directory or the GitHub repository in which you want to keep the file.

#### Edit an XML file

1. Click **File > Open From > Device**.

2. Find the **.xml** file that you want to edit and open the file.

3. After you edit the file, delete the old **.xml** file and **.png** file from your directory or GitHub repository, and save both versions of the file by using the the same processes described earlier in this section.

  **Note:** When you edit and save an existing draw.io file, the old file name is not overwritten. Instead, a number is appended to the end of the file name; for example, **filename1.xml**. If you do not want duplicate files, delete the old files before you save your edits.

### Best practices for diagrams
Following are some suggestions to help you make a professional diagram.

#### Avoid using stencils or symbols with a cloud border
Diagrams contained within our documentation should emphasize education. A cloud border adds no inherent educational value to a stencil or symbol.

**Use**

![Acceptable use of cloud shape](https://github.com/rackerlabs/docs-rackspace/blob/master/_assets/img/images.png)

**Avoid**

![Unacceptable use of cloud shape](https://github.com/rackerlabs/docs-rackspace/blob/master/_assets/img/cloud-images-do-not-use.png)

#### Use round corners on lines
Lines occasionally need to change direction to show a relationship between two stencils. In the **Format Panel** under **Style** in draw.io, set the drop-down menu to **Rounded**.
