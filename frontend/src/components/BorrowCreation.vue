<template>
    <v-container>
        <v-form @submit.prevent="createBorrow">
            <v-select v-model="borrow.user_id" :items="users" item-text="name" item-value="id" label="Select User"
                required />
            <v-select v-model="borrow.book_id" :items="books" item-text="name" item-value="id" label="Select Book"
                required />
            <v-btn class="mt-2" color="primary" type="submit" block>Borrow Book</v-btn>
        </v-form>
    </v-container>
</template>

<script>
export default {
    data() {
        return {
            borrow: {
                user_id: null,
                book_id: null,
            },
            books: [],
            users: [],
        };
    },
    created() {
        this.fetchBooks();
        this.fetchUsers();
    },
    methods: {
        async fetchBooks() {
            try {
                const response = await fetch('http://localhost:4000/books');
                const data = await response.json();
                this.books = data.books.filter(book => book.is_available).map(book => ({
                    id: book.id,
                    name: book.name,
                }));
            } catch (error) {
                console.error('Error fetching books:', error);
            }
        },
        async fetchUsers() {
            try {
                const response = await fetch('http://localhost:4000/users');
                const data = await response.json();
                this.users = data.users.map(user => ({
                    id: user.id,
                    name: user.username,
                }));
            } catch (error) {
                console.error('Error fetching users:', error);
            }
        },
        async createBorrow() {
            try {
                const response = await fetch('http://localhost:4000/borrows/new', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(this.borrow),
                });

                if (response.ok) {
                    this.borrow = {
                        user_id: null,
                        book_id: null,
                    };
                    this.fetchBooks();
                } else {
                    console.error('Error creating book');
                }
            } catch (error) {
                console.error('Error creating book:', error);
            }
        },
    },
};
</script>