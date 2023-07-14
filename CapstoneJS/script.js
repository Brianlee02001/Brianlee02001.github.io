// Blog Post class
class Post {
  constructor(id, title, content) {
    this.id = id;
    this.title = title;
    this.content = content;
    this.timestamp = new Date();
  }
}

// Blog class
class Blog {
  constructor() {
    this.posts = [];
  }

  addPost(post) {
    this.posts.unshift(post);
  }

  deletePost(id) {
    const index = this.posts.findIndex(post => post.id === id);
    if (index !== -1) {
      this.posts.splice(index, 1);
    }
  }

  getPosts() {
    return this.posts;
  }
}

// Create a new Blog instance
const blog = new Blog();

// DOM elements
const createPostForm = document.getElementById('create-post-form');
const postsList = document.getElementById('posts');

// Function to display posts
function displayPosts() {
  postsList.innerHTML = '';

  blog.getPosts().forEach(post => {
    const postItem = document.createElement('li');
    postItem.className = 'post';
    postItem.innerHTML = `
      <h3>${post.title}</h3>
      <p>${post.content}</p>
      <small>${post.timestamp.toLocaleString()}</small>
      <div class="actions">
        <button class="delete-btn" data-id="${post.id}">Delete</button>
      </div>
    `;
    postsList.appendChild(postItem);
  });
}

// Event listener for the create post form
createPostForm.addEventListener('submit', event => {
  event.preventDefault();

  const titleInput = document.getElementById('title');
  const contentInput = document.getElementById('content');

  const title = titleInput.value;
  const content = contentInput.value;

  if (title && content) {
    const id = Date.now().toString();
    const post = new Post(id, title, content);
    blog.addPost(post);

    titleInput.value = '';
    contentInput.value = '';

    displayPosts();
  }
});

// Event delegation for delete button
postsList.addEventListener('click', event => {
  const target = event.target;
  
  if (target.classList.contains('delete-btn')) {
    const postId = target.getAttribute('data-id');
    blog.deletePost(postId);
    displayPosts();
  }
});

// Initial display of posts
displayPosts();