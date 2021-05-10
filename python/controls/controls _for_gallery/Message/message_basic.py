import pglet
from pglet import Stack, Text, Message

page = pglet.page()

stack = Stack(width='70%', gap=20, controls=[
    Text('Messages', size='xLarge'),
    Message(value='This is just a message.'),
    Message(value='Success message with dismiss button', dismiss=True, type='success'),
    Message(value='Error message with dismiss button', dismiss=True, type='Error'),
    Message(type='blocked', truncated=True, dismiss=True, value='Blocked Message - single line, with dismiss button and truncated text. Truncation is not available if you use action buttons or multiline and should be used sparingly. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi luctus, purus a lobortis tristique, odio augue pharetra metus, ac placerat nunc mi nec dui. Vestibulum aliquam et nunc semper scelerisque. Curabitur vitae orci nec quam condimentum porttitor et sed lacus. Vivamus ac efficitur leo. Cras faucibus mauris libero, ac placerat erat euismod et. Donec pulvinar commodo odio sit amet faucibus. In hac habitasse platea dictumst. Duis eu ante commodo, condimentum nibh pellentesque, laoreet enim. Fusce massa lorem, ultrices eu mi a, fermentum suscipit magna. Integer porta purus pulvinar, hendrerit felis eget, condimentum mauris. You\'ve been warned!'),

])

page.add(stack)