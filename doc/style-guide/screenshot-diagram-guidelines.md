# Screenshot and diagram guidelines

At Rackspace, we strive to deliver ***Fanatical Support***® through
exceptional documentation. Images are an essential part of helpful, clear, and
concise content. Follow the standards in this section when creating images for
your documents.

- [Screenshot guidelines](#screenshot-guidelines)
- [Diagram guidelines](#diagram-guidelines)

**Note:** These guidelines conform to all of the rules outlined in the [writing
style guide](basic-writing-guidelines.md).

## Screenshot guidelines and process

When your content references a user interface (UI), consider whether you need
to include screenshots. Screenshots can be helpful when text alone cannot
adequately convey instructions, and users like screenshots and find them
useful. However, screenshots are difficult and time-consuming to maintain and
present translation problems. Therefore, the use of screenshots within your
article should be kept to a minimum.

- [Screenshot alternatives](#screenshot-alternatives)
- [When to use screenshots](#when-to-use-screenshots)
- [When not to use screenshots](#when-not-to-use-screenshots)
- [Before you create a screenshot](#before-you-create-a-screenshot)
- [Screenshots in procedures](#screenshots-in-procedures)
- [Screenshot checklist](#screenshot-checklist)

### Screenshot alternatives

As an alternative to screenshots, use the correct names of the UI labels with
which the user must interact and the values that they must choose or enter.
Show the names of buttons, options, check boxes, menus, windows, dialog boxes,
and so on as they appear on the UI. For example, for straightforward
instructions like, "To open a file, select **File > Open**," a screenshot is
not required.

### When to use screenshots

You can use screenshots for the following purposes:

- Orient users in a complicated or long procedure

- Show complex windows or dialog boxes, such as those that contain multiple
  subsets of information, with free-form text fields and many options available
  for selection

### When not to use screenshots

Do not include screenshot of the following items:

- Code samples (instead, show code samples in code blocks)

- Dialog boxes that are easy to understand, such as drop-down lists and option
  buttons with few or no free-form text fields

- Confirmation boxes

- License agreement boxes

- Message text (instead show message text within regular text)

- Progress bars

- Welcome windows

- Wizard pages, especially Welcome pages and other simple pages

- Tables created in another authoring tool

### Before you create a screenshot

Install Jing to capture and edit screenshots. [Jing is available as a free
download](https://www.techsmith.com/jing.html).

To learn how to take a screenshot and make a callout, use the Jing [capture an
image](https://www.techsmith.com/tutorial-jing-capture-an-image.html) tutorial.

**Note:** Jing does not support Linux distributions, but you can use other
programs such as gscreendemp, GreenShot, and Shutter on Linux.

### Screenshots in procedures

If you include a screenshot in a procedure, place it directly under the step
that it illustrates. Do not rely on the screenshot to show information or
values that the user must enter; always provide that information in the text of
the steps. However, ensure that the screenshot accurately reflects the
directions and values in the step text.

### Screenshot checklist

Use the following standards when creating your screenshots:

- [ ] **Size**: Make screenshots no larger than 600 pixels wide.
- [ ] **Callouts**: Use only arrows and boxes for callouts.
- [ ] **Scope**: Limit the scope of a screenshot to just the portion of the UI
  that shows the action, plus enough surrounding detail to help the user locate
  the item.
- [ ] **Callout color**: Use **Red** (hexadecimal color **FF0000**) for all
  callouts.
- [ ] **File name**: Create unique and meaningful file names to easily
  differentiate between screenshots.
- [ ] **Titles:** Titles are not required, especially for screenshots in
  procedures and tutorials. If you want to add a title to a screenshot for
  clarity, follow the guidelines in [Titles and
  headings](m-z-style-guidelines.md).

To learn how to take a screenshot and make a callout in Jing, use the tutorial
[capture an
image](https://www.techsmith.com/tutorial-jing-capture-an-image.html)

## Diagram guidelines

Diagrams can be useful tools to help users visualize complex processes in a
simplified fashion. However, diagrams can sometimes be too simplistic,
confusing the user instead of providing help. The decision about whether a
diagram might be helpful depends on the context of each document and the
discretion of each writer.

- [When to use diagrams](#when-to-use-diagrams)
- [When not to use diagrams](#when-not-to-use-diagrams)
- [Before you create a diagram](#before-you-create-a-diagram)
- [Diagram checklist](#diagram-checklist)

### When to use diagrams

Include diagrams in the following situations:

- When there is evidence of a process, whether the process is automated or
  manual

- When you need to clarify configurations and settings, such as the
  architecture for virtual servers

- When you need to define a complex workflow within a Rackspace product

### When not to use diagrams

Do not include diagrams in the following situations:

- When a workflow is too simplistic, such as using the control panel to create
  a cloud server

- When there is no interaction with a Rackspace product

### Before you create a diagram

To create diagrams, you need to access the recommended software and download
the required icons and stencils.

#### Software

Use [draw.io](https://www.draw.io/) to create your diagrams. Draw.io enables
you to create diagrams directly in your web browser of choice.

To get started with draw.io, see the instructions in the [Draw.io Online User
Manual](https://support.draw.io/display/DO/Draw.io+Online+User+Manual).

#### Icons, stencils, and shapes

Download Rackspace's library of product icons and stencils. These icons and
stencils are considered **objects**.

- The product icons are blue and are located in [this zip
  file](https://github.com/rackerlabs/docs-rackspace/blob/master/doc/style-guide/images/zip/ProductIcons.zip).

- Stencils are used to represent certain functions and hardware such as the
  world wide web or a server. These stencils are black and are located in [this
  zip
  file](https://github.com/rackerlabs/docs-rackspace/blob/master/doc/style-guide/images/zip/RackspaceDiagramIcons.zip).

After you download the icons and stencils, you can being making diagrams in
Draw.io.

### Diagram checklist

Use the following standards when creating diagrams:

#### Properties

Each diagram property is located on the right of the Draw.io main screen under
**Diagrams**.

- [ ] **Paper size**: Set the paper size to **A4 (210 mm x 297 mm)** and
  **Landscape**.

- [ ] **Background color**: Set the background color to **none**.

- [ ] **File format**: Save all diagrams saved as editable SVG files.

   1. Click **File > Save As**.
   2. Type a descriptive name for the file, and
   replace `.xml` with `.svg` at the end of the file name. The file is saved to
   your local directory.

- [ ] **File name**: Create unique and meaningful file names to differentiate
  diagrams.

#### Text formatting

- [ ] **Font**: Set the font to **Helvetica**.

- [ ] **Titles:** Title must be **bolded**, aligned **left**, and be at least
  **24px** in size.

#### Objects

- [ ] **Product icons**: An icon represents it's corresponding product. Product
  icons are always blue.

   ![Cloud Images stencil](images/img/images.png)

   **Note:** If you find a Rackspace product icon that is not blue, email
   how-to@rackspace.com and a member of our team will create a blue version of
   the icon.

- [ ] **Stencils**: A stencil represents a concept or function. Stencils that
  are *not* Rackspace products should always appear in black.

- [ ] **Labels**: Label all product icons, stencils, and shapes, must be
  labeled according to their function within the diagram.

#### Lines and arrows

- [ ] **Line usage**: Use lines are used to connect and display a relationship
  between two or more objects.

- [ ] **Line width**: Line width must be at least **2pt**. You can change the
  width of a line in the **Format Panel** under **Style** when you select the
  line.

- [ ] **Line shape**: Keep lines straight unless a line needs to change
  direction.

- [ ] **Rounded line corners**: If a line changes direction, the corner in
  which the change of direction occurs must be rounded. You can change to
  rounded corners by selecting the line, going to the **Format Panel** under
  **Style**, and selecting **Rounded** in the dropdown menu.

- [ ] **Solid lines**: Use solid lines to show a direct relationship between
  objects, as shown in the example below.

   ![Example of solid lines](images/img/solid-lines.png)

- [ ] **Dashed lines**: Use dashed lines to group objects that are connected
  through a network, as shown in the example below.

   ![Example of dashed lines](images/img/dashed-lines.png)

- [ ] **Dotted lines**: Use dotted lines to show how data entered by the user
  travels, as shown in the example below.

   ![Example of dotted lines](images/img/dotted-lines.png)

- [ ] **One-way and two-way arrows:** Use arrows to represent direct
  interactions between two or more stencils. If a stencil is attached to an
  arrow, it implies that the product represented by the stencil needs to
  interact with another piece of the diagram.

   In the following example, the CDN management service needs to interact with
   the CDN to perform its function. Similarly, the CDN needs to be managed by
   the CDN management service. The relationship is two-way, so the line has
   arrows on both ends pointed to both stencils.

   ![Example of one-way and two-way arrows](images/img/arrowsscreenshot.png)

## Next steps

- [Contribute to our Rackspace How-To support
  network](https://github.com/rackerlabs/rackspace-how-to)

- [Contribute to our Rackspace core infrastructure user
  guide](https://github.com/rackerlabs/docs-core-infra-user-guide)
