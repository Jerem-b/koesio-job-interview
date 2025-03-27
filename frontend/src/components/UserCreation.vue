<template>
    <v-container>
        <v-form @submit.prevent="createUser">
            <v-text-field v-model="user.username" label="User name" required></v-text-field>
            <v-text-field v-model="user.password" label="Password" required type="password"></v-text-field>
            <v-btn class="mt-2" color="primary" type="submit" block>Create User</v-btn>
        </v-form>
    </v-container>
</template>

<script>
export default {
    data() {
        return {
            user: {
                username: "",
                password: "",
            }
        };
    },
    methods: {
        async createUser() {
            try {
                const response = await fetch(
                    'http://localhost:4000/register', {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(this.user),
                }
                );
                if (!response.ok) throw new Error("Failed to create author");
                await response.json();
                if (response.ok) {
                    this.user = {
                        username: '',
                        password: '',
                    };
                }
            } catch (error) {
                console.error("Error:", error);
            }
        }
    },
};
</script>